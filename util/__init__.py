
class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """
    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost=1, deletion_cost=1, subst_cost=1):
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost

    def distance(source, target, m, n):
        """
        Calculates the distance between two strings.
        :param source: The source string
        :param target: The target string
        :param m: The length of the source string
        :param n: The length of the target string
        :return: The scalar distance between the source and target.
        """
        dp = [[0 for x in range(n+1)] for x in range(m+1)] 
        for i in range(m+1): 
            for j in range(n+1): 

                if i == 0: 
                    dp[i][j] = j 

                elif j == 0: 
                    dp[i][j] = i 

                elif str1[i-1] == str2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] 
                else: 
                    dp[i][j] = 1 + min(dp[i][j-1],	 # Insert 
                                    dp[i-1][j],	 # Remove 
                                    dp[i-1][j-1]) # Replace 

        return dp[m][n] 

str1 = input("Enter first string ")
str2 = input("Enter second string ")

print(distance(str1, str2, len(str1), len(str2))) 
