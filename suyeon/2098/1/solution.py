import sys
input = sys.stdin.readline
# https://shoark7.github.io/programming/algorithm/solve-tsp-with-dynamic-programming
N = int(input())

dists = [] * N
for i in range(N):
    dists.append(list(map(int, input().split())))

'''
pseudo code
def find_path(start, last, visited, accumulated_cost):
    if all visited:
        returning_cost = D[last][start] or inf
        ans = min(ans, accumulated_cost + returning_cost)
        return
    
    for left_city in visited의 여집합:
        if last 와 left_city 연결됨:
            visited[left_city] = True
            find_path(s, left_city, visited, accumulated_cost + D[last][left_city])
            visited[left_city] = False
    '''

def tsp():
    VISITED_ALL =  (1 << N) - 1 
    '''
    N개의 도시를 모두 방문해서 1...1이 된 상황
        1 << 10 = 100       (이진수)
        1 << 10 - 1 = 11    (이진수)
    '''

    cache = [[None] * (1 << N) for _ in range(N)]

    '''
    a << b : 이진수 a의 각 자리를 b자리 앞으로 (뒤에 0을 b개 붙임) = N번째 비트 켜기

    for _ in range(N) =>  N개의 도시에 대해서(N행),
    1 << N은 을 통해 맨 앞 1을 제외한 뒤쪽 N개의 자릿수가 각 도시를 표현할 수 있도록 해주자 (10000)
    '''
    INF = float('inf')  # 양의 무한대 

    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF
            # 모든 도시를 방문했다면 1111일 것이고, last 와 시작도시(0번째도시) 사이의 경로가 존재한다면 그 비용을 리턴하고, 이어져있지 않다면 무한대를 리턴한다. 

        if cache[last][visited] is not None:
            # last 와 visited 사이의 거리가 이미 연산이 완료되었다면, 바로 그 값을 반환
            return cache[last][visited]

        tmp = INF
        # 거리를 무한대로 두고,

        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                ''' 
                방문한 도시목록(visited)와 왼쪽 도시 하나 방문 (1 << city)한 것을 &연산한 값이 0 이면 city는 아직 방문하지 않은 도시이다.
                가장 최근에 방문한 도시(last)와 city가 연결되어있다면 방문시켜주자
                '''

                tmp = min(
                    tmp,
                    find_path(city, visited | (1 << city)) + dists[last][city]
                    )
                '''
                무한대로 설정했던 tmp를 새로운 값으로 갱신시켜주자.
                재귀호출시 최근 방문지점은 현재의 city가 되고, visited에는 현재 도시가 추가된다.  (or연산시 모든 방문한 자릿수의 값(1)이 살아남음)

                find_path 가 비용을 리턴하게 하고 그 결과값에 dists[last][city] 를 더해주자.

                '''
        cache[last][visited] = tmp  # 새로 갱신된 값으로 cache의 last, visited자릿수 값을 바꿔줌
        return tmp
    return find_path(0, 1 << 0)  # 가장 오른쪽 도시만 방문

print(tsp())
tsp()