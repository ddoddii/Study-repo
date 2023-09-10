# 2. Calculate Mail Arrive Time 
# n : 전송 시간, m : 서버에서 작업 시간
# errorlog 1: 전송실패 (전송 실패로 결과는 -1), 2: 전송지연 (전송 지연되면 남은 작업시간 *2 )
# 생각해야 하는 case : server_send 이 계속 delay_time 이후로 조정되는 케이스 (계속 server_send 를 업데이트 해야 함)


n = 1
m = 5
send = [1,2,3,4,6]
errorlog = [[2,6],[2,8],[2,16]]
# result = [9, 13, 17, 25, 17]

def solution(n,m,send,errorlog):
    delay_times, fail_times = [] , []
    for error in errorlog:
        if error[0] == 1:
            fail_times.append(error[1])
        else:
            delay_times.append(error[1])
    answer = []
    for s in send:
        server_arrive = s + n
        server_send = server_arrive + m
        for delay_time in delay_times:
            if server_send > delay_time and server_arrive <= delay_time :
                left_time = server_send - delay_time
                left_time *= 2
                server_send = delay_time + left_time

        send = True
        
        for fail_time in fail_times:
            if server_send > fail_time and server_arrive <= fail_time:
                send = False
        if send :
            fin_time = server_send + n
        else:
            fin_time = -1
        answer.append(fin_time)
    return answer

print(solution(n,m,send,errorlog))
    
