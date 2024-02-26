class Question:
    def __init__(self, id, marks, time):
        self.id = id
        self.marks = marks
        self.time = time

def create_question(id, marks, time):
    return Question(id, marks, time)

def compare(a, b):
    return (a.marks / a.time) > (b.marks / b.time)

def main():
    m = 120 
    t = 20
    n = 5

    questions = [(20, 10), (20, 5), (30, 5), (30, 6), (20, 40)]
    que_list = [create_question(i + 1, marks, time) for i, (marks, time) in enumerate(questions)]
    que_list.sort(key=lambda x: x.marks / x.time, reverse=True)

    total_marks_alone = 0
    total_marks_with_friend = 0
    current_time_alone = 0
    current_time_with_friend = 0

    for ques in que_list:
        if current_time_alone + ques.time <= t:
            print(f"ques {ques.id} 100% done  -- {ques.marks} marks")
            total_marks_alone += ques.marks
            current_time_alone += ques.time
        elif current_time_alone < t:
            remaining_time = t - current_time_alone
            fraction = remaining_time / ques.time
            partial_marks = int(fraction * ques.marks)
            print(f"ques {ques.id} {fraction * 100}% done  -- {partial_marks} marks")
            total_marks_alone += partial_marks
            current_time_alone += remaining_time


        time_for_question = ques.time // 2
        if current_time_with_friend + time_for_question <= t:
            total_marks_with_friend += ques.marks
            current_time_with_friend += time_for_question
        elif current_time_with_friend < t:
            remaining_time = t - current_time_with_friend
            fraction = remaining_time / time_for_question
            partial_marks = int(fraction * ques.marks)
            total_marks_with_friend += partial_marks
            current_time_with_friend += remaining_time

    print(f"Maximum marks answering with a friend: {total_marks_with_friend} marks")

main()