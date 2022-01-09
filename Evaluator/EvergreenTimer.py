#!/usr/bin/python3

# Add import statement for your algorithm here
import NullMove as nm
import chess

# Change this to your algorithm
algo = nm.NullMove()

# Increase the maximum depth if you are confident that your algorithm is fast
depth = 4

# Increase iterations per position to get more accurate "average running time" 
iteration = 3




# Tweak the code below if you know what you are doing, else just leave it be
# We're going to time the running duration of our algorithm
# By making it evaluate the whole Evergreen game, position by position






# All the positions of Evergreen's game
# It looks intimidating, but it's easier work than calling subscript and get its output
evergreen_pos = [
"rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",
"rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
"rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
"r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
"r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3",
"r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4",
"r1bqk1nr/pppp1ppp/2n5/2b1p3/1PB1P3/5N2/P1PP1PPP/RNBQK2R b KQkq - 0 4",
"r1bqk1nr/pppp1ppp/2n5/4p3/1bB1P3/5N2/P1PP1PPP/RNBQK2R w KQkq - 0 5",
"r1bqk1nr/pppp1ppp/2n5/4p3/1bB1P3/2P2N2/P2P1PPP/RNBQK2R b KQkq - 0 5",
"r1bqk1nr/pppp1ppp/2n5/b3p3/2B1P3/2P2N2/P2P1PPP/RNBQK2R w KQkq - 1 6",
"r1bqk1nr/pppp1ppp/2n5/b3p3/2BPP3/2P2N2/P4PPP/RNBQK2R b KQkq - 0 6",
"r1bqk1nr/pppp1ppp/2n5/b7/2BpP3/2P2N2/P4PPP/RNBQK2R w KQkq - 0 7",
"r1bqk1nr/pppp1ppp/2n5/b7/2BpP3/2P2N2/P4PPP/RNBQ1RK1 b kq - 1 7",
"r1bqk1nr/pppp1ppp/2n5/b7/2B1P3/2Pp1N2/P4PPP/RNBQ1RK1 w kq - 0 8",
"r1bqk1nr/pppp1ppp/2n5/b7/2B1P3/1QPp1N2/P4PPP/RNB2RK1 b kq - 1 8",
"r1b1k1nr/pppp1ppp/2n2q2/b7/2B1P3/1QPp1N2/P4PPP/RNB2RK1 w kq - 2 9",
"r1b1k1nr/pppp1ppp/2n2q2/b3P3/2B5/1QPp1N2/P4PPP/RNB2RK1 b kq - 0 9",
"r1b1k1nr/pppp1ppp/2n3q1/b3P3/2B5/1QPp1N2/P4PPP/RNB2RK1 w kq - 1 10",
"r1b1k1nr/pppp1ppp/2n3q1/b3P3/2B5/1QPp1N2/P4PPP/RNB1R1K1 b kq - 2 10",
"r1b1k2r/ppppnppp/2n3q1/b3P3/2B5/1QPp1N2/P4PPP/RNB1R1K1 w kq - 3 11",
"r1b1k2r/ppppnppp/2n3q1/b3P3/2B5/BQPp1N2/P4PPP/RN2R1K1 b kq - 4 11",
"r1b1k2r/p1ppnppp/2n3q1/bp2P3/2B5/BQPp1N2/P4PPP/RN2R1K1 w kq - 0 12",
"r1b1k2r/p1ppnppp/2n3q1/bQ2P3/2B5/B1Pp1N2/P4PPP/RN2R1K1 b kq - 0 12",
"1rb1k2r/p1ppnppp/2n3q1/bQ2P3/2B5/B1Pp1N2/P4PPP/RN2R1K1 w k - 1 13",
"1rb1k2r/p1ppnppp/2n3q1/b3P3/Q1B5/B1Pp1N2/P4PPP/RN2R1K1 b k - 2 13",
"1rb1k2r/p1ppnppp/1bn3q1/4P3/Q1B5/B1Pp1N2/P4PPP/RN2R1K1 w k - 3 14",
"1rb1k2r/p1ppnppp/1bn3q1/4P3/Q1B5/B1Pp1N2/P2N1PPP/R3R1K1 b k - 4 14",
"1r2k2r/pbppnppp/1bn3q1/4P3/Q1B5/B1Pp1N2/P2N1PPP/R3R1K1 w k - 5 15",
"1r2k2r/pbppnppp/1bn3q1/4P3/Q1B1N3/B1Pp1N2/P4PPP/R3R1K1 b k - 6 15",
"1r2k2r/pbppnppp/1bn5/4Pq2/Q1B1N3/B1Pp1N2/P4PPP/R3R1K1 w k - 7 16",
"1r2k2r/pbppnppp/1bn5/4Pq2/Q3N3/B1PB1N2/P4PPP/R3R1K1 b k - 0 16",
"1r2k2r/pbppnppp/1bn5/4P2q/Q3N3/B1PB1N2/P4PPP/R3R1K1 w k - 1 17",
"1r2k2r/pbppnppp/1bn2N2/4P2q/Q7/B1PB1N2/P4PPP/R3R1K1 b k - 2 17",
"1r2k2r/pbppnp1p/1bn2p2/4P2q/Q7/B1PB1N2/P4PPP/R3R1K1 w k - 0 18",
"1r2k2r/pbppnp1p/1bn2P2/7q/Q7/B1PB1N2/P4PPP/R3R1K1 b k - 0 18",
"1r2k1r1/pbppnp1p/1bn2P2/7q/Q7/B1PB1N2/P4PPP/R3R1K1 w - - 1 19",
"1r2k1r1/pbppnp1p/1bn2P2/7q/Q7/B1PB1N2/P4PPP/3RR1K1 b - - 2 19",
"1r2k1r1/pbppnp1p/1bn2P2/8/Q7/B1PB1q2/P4PPP/3RR1K1 w - - 0 20",
"1r2k1r1/pbppRp1p/1bn2P2/8/Q7/B1PB1q2/P4PPP/3R2K1 b - - 0 20",
"1r2k1r1/pbppnp1p/1b3P2/8/Q7/B1PB1q2/P4PPP/3R2K1 w - - 0 21",
"1r2k1r1/pbpQnp1p/1b3P2/8/8/B1PB1q2/P4PPP/3R2K1 b - - 0 21",
"1r4r1/pbpknp1p/1b3P2/8/8/B1PB1q2/P4PPP/3R2K1 w - - 0 22",
"1r4r1/pbpknp1p/1b3P2/5B2/8/B1P2q2/P4PPP/3R2K1 b - - 1 22",
"1r2k1r1/pbp1np1p/1b3P2/5B2/8/B1P2q2/P4PPP/3R2K1 w - - 2 23",
"1r2k1r1/pbpBnp1p/1b3P2/8/8/B1P2q2/P4PPP/3R2K1 b - - 3 23",
"1r3kr1/pbpBnp1p/1b3P2/8/8/B1P2q2/P4PPP/3R2K1 w - - 4 24",
"1r3kr1/pbpBBp1p/1b3P2/8/8/2P2q2/P4PPP/3R2K1 b - - 0 24"]

# Evaluate the game many times, each time with increasing depth
for depth_i in range(1, depth+1):

    result = "Depth " + str(depth_i) + ": "

    # Evaluate each position of the game many time, and takes average time
    for pos_i in evergreen_pos:
        TotalTime = 0
        for ite_i in range (0, iteration):
            TotalTime += algo.GetEvaluateTime(chess.Board(pos_i), depth_i)[0]
        result += "\n" + "{:1.2e}".format(TotalTime/iteration) + " secs"

    print(result)
    print()
        

            


