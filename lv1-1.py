def solution(schedules, timelogs, startday):

    def to_minutes(time_int):
        hour = time_int // 100
        minute = time_int % 100

        return hour * 60 + minute


    answer = 0
    num_employees = len(schedules)

    for i in range(num_employees):
        schedule = schedules[i]
        timelog = timelogs[i]

        allowed_minutes = to_minutes(schedule) + 10
        
        is_eligible = True 
        
        for j in range(7):

            current_day = (startday - 1 + j) % 7 + 1

            if current_day in [1, 2, 3, 4, 5]:
                
                actual_minutes = to_minutes(timelog[j])

                if actual_minutes > allowed_minutes:
                    is_eligible = False
                    break
        if is_eligible:
            answer += 1
            
    return answer