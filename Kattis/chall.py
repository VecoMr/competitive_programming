import math
s = input()
# Python3 program for the above approach
import numpy as np

# Function to find the LCS
# of strings S and string T
def LCS(S, N, T, M, dp) :

	# Base Case
	if (N == 0 or M == 0) :
		return 0;

	# Already Calculated State
	if (dp[N][M] != 0) :
		return dp[N][M];

	# If the characters are the same
	if (S[N - 1] == T[M - 1]) :
		dp[N][M] = 1 + LCS(S, N - 1, T, M - 1, dp);
		return dp[N][M]
	# Otherwise
	dp[N][M] = max( LCS(S, N - 1, T, M, dp), LCS(S, N, T, M - 1, dp));
	return dp[N][M]


# Function to find the minimum number of
# characters that needs to be appended
# in the string to get all lowercase
# alphabets as a subsequences
def minimumCharacter(S) :

	# String containing all the characters
	T = "abcdefghijklmnopqrstuvwxyz";

	N = len(S); M = len(T);

	# Stores the result of overlapping
	# subproblems
	dp = np.zeros((N + 1, M + 1));
	# Return the minimum characters
	# required
	return (26 - LCS(S, N, T, M, dp));

print(minimumCharacter(s))