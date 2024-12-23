
if __name__ == "__main__":

    with open("puzzle.txt") as f:
        puzzle = [tuple(row.strip().split('-')) for row in f]
        
        graph = {}
        for (x, y) in puzzle:
            graph.setdefault(x, []).append(y)
            graph.setdefault(y, []).append(x)

        def part_1():
            parties = set()
            for k, v in graph.items():
                partie = set()
                partie.add(k)
                for i, goal in enumerate(v):
                    partie.add(goal)
                    for j in range(i + 1, len(v)):
                        if v[j] in graph[goal]:
                            partie.add(v[j])
                            partie = set(sorted(partie))
                            if len(partie) == 3:
                                parties.add(tuple(partie))
                                partie.remove(v[j])
                    partie.remove(goal)

            start_with_t = []
            for partie in parties:
                if any(pc.startswith('t') for pc in partie):
                    start_with_t.append(partie)

            print(f"Answer part 1 --> {len(start_with_t)}")

        def part_2():
            LAN = 1
            while True:
                parties = set()
                for k, v in graph.items():
                    partie = [k]
                    for i, goal in enumerate(v):
                        if any(goal not in graph[p] for p in partie):
                            continue
                        partie.append(goal)
                        for j in range(i + 1, len(v)):
                            if v[j] in graph[goal]:
                                if any(v[j] not in graph[p] for p in partie):
                                    continue
                                partie.append(v[j])
                                if len(partie) == LAN:
                                    parties.add(tuple(sorted(partie)))
                                    [partie.pop() for _ in range(LAN - 2)]

                        partie.pop()
                
                if len(parties) == 1:
                    print(f"Answer part 2 --> {','.join(parties.pop())}")
                    break
                LAN += 1
            
        part_1(), part_2()

                    






