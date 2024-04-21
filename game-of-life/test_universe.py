from game_of_life import Universe


def display(universe):
    for i in range(universe.max_row):
        print(str(universe.board[i]))


def test_block_still():
    universe = Universe(5, 5, [(1, 1), (1, 2), (2, 1), (2, 2)])
    print('\nBefore:')
    display(universe)

    before = universe.board
    universe.update()
    after = universe.board
    print('\nAfter:')
    display(universe)

    assert before == after


def test_bee_hive_still():
    universe = Universe(6, 5, [(1, 2), (2, 1), (3, 1), (4, 2), (2, 3), (3, 3)])
    print('\nBefore:')
    display(universe)

    before = universe.board
    universe.update()
    after = universe.board
    print('\nAfter:')
    display(universe)

    assert before == after


def test_loaf_still():
    universe = Universe(6, 6, [(2, 1), (3, 1), (1, 2), (4, 2), (2, 3), (4, 3), (3, 4)])
    print('\nBefore:')
    display(universe)

    before = universe.board
    universe.update()
    after = universe.board
    print('\nAfter:')
    display(universe)

    assert before == after


def test_boat_still():
    universe = Universe(5, 5, [(1, 1), (2, 1), (1, 2), (3, 2), (2, 3)])
    print('\nBefore:')
    display(universe)

    before = universe.board
    universe.update()
    after = universe.board
    print('\nAfter:')
    display(universe)

    assert before == after


def test_tub_still():
    universe = Universe(5, 5, [(2, 1), (1, 2), (3, 2), (2, 3)])
    print('\nBefore:')
    display(universe)

    before = universe.board
    universe.update()
    after = universe.board
    print('\nAfter:')
    display(universe)

    assert before == after


def test_blinker_oscillator():
    universe = Universe(5, 5, [(1, 2), (2, 2), (3, 2)])
    print('\nBefore:')
    display(universe)

    period = 2
    before = universe.board
    for _ in range(period - 1):
        universe.update()
        print('\nAfter:')
        display(universe)
        assert before != universe.board

    universe.update()
    assert before == universe.board


def test_penta_decathlon_oscillator():
    universe = Universe(11, 18, [])
    universe.seed([(4, 6), (4, 11),
                   (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (5, 10), (5, 12), (5, 13),
                   (6, 6), (6, 11)])
    print('\nBefore:')
    display(universe)

    period = 15
    before = universe.board
    for i in range(period - 1):
        universe.update()
        print(f'\nGeneration {i + 1}:')
        display(universe)
        assert before != universe.board

    universe.update()
    assert before == universe.board


def test_diehard_pattern():
    universe = Universe(50, 50, [])
    shift_right = 10
    shift_down = 10
    universe.seed([(7 + shift_right, 1 + shift_down),
                   (1 + shift_right, 2 + shift_down), (2 + shift_right, 2 + shift_down),
                   (2 + shift_right, 3 + shift_down), (6 + shift_right, 3 + shift_down),
                   (7 + shift_right, 3 + shift_down), (8 + shift_right, 3 + shift_down)])
    print('\nBefore:')
    display(universe)

    expected = [[0] * universe.max_col for _ in range(universe.max_row)]
    generations = 130
    for i in range(generations - 1):
        universe.update()
        print(f'\nGeneration {i + 1}:')
        display(universe)
        assert expected != universe.board

    universe.update()
    assert expected == universe.board

