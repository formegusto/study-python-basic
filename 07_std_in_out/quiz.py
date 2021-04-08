for week in range(1, 51):
    with open("quiz_dir/{0}주차.txt".format(week), "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(week))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")
