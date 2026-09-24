"""Exhaustively check a small, explicitly idealized authority system.
No AI models, human participants, or empirical safety claims are involved.
"""
from __future__ import annotations
import argparse
import itertools
import json
from collections import deque
from pathlib import Path

DOMAINS = ('operator', 'authorizer', 'reviewer')
VARIANTS = ('protected', 'mutable_policy', 'direct_bypass')
START = (False,) * 6  # proposed, logged, authorized, reviewed, committed, relaxed


def successors(state, coalition, variant):
    p, l, a, r, c, m = state
    if c:
        return
    def changed(index):
        out = list(state)
        out[index] = True
        return tuple(out)
    if 'operator' in coalition:
        if not p:
            yield 'propose', changed(0)
        if p and not l:
            yield 'record', changed(1)
        if p and l and (m or (a and r)):
            yield 'execute', changed(4)
        if variant == 'mutable_policy' and not m:
            yield 'relax_policy', changed(5)
        if variant == 'direct_bypass' and p and l:
            yield 'bypass', changed(4)
    if 'authorizer' in coalition and p and not a:
        yield 'authorize', changed(2)
    if 'reviewer' in coalition and p and not r:
        yield 'review', changed(3)


def explore(coalition, variant):
    queue = deque([START])
    paths = {START: []}
    while queue:
        state = queue.popleft()
        for action, target in successors(state, coalition, variant):
            if target not in paths:
                paths[target] = paths[state] + [action]
                queue.append(target)
    traces = [path for state, path in paths.items() if state[4]]
    witness = min(traces, key=lambda t: (len(t), t)) if traces else None
    return {'coalition': list(coalition), 'reachable_states': len(paths),
            'can_commit': bool(traces), 'shortest_witness': witness}


def run():
    results = {'scope': 'Exhaustive Boolean toy model; not empirical AI evidence.',
               'state_bits': 6, 'domains': list(DOMAINS), 'variants': {}}
    coalitions = [c for n in range(4) for c in itertools.combinations(DOMAINS, n)]
    for variant in VARIANTS:
        cases = [explore(c, variant) for c in coalitions]
        expected = [len(c) == 3 if variant == 'protected' else 'operator' in c
                    for c in coalitions]
        assert [c['can_commit'] for c in cases] == expected
        successful = [c for c in cases if c['can_commit']]
        results['variants'][variant] = {
            'cases': cases, 'successful_coalitions': len(successful),
            'minimum_domains_to_commit': min(len(c['coalition']) for c in successful)}
    assert not explore(('operator', 'authorizer'), 'protected')['can_commit']
    assert not explore(('operator', 'reviewer'), 'protected')['can_commit']
    assert explore(DOMAINS, 'protected')['can_commit']
    results['total_coalition_checks'] = 24
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text)
