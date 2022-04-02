def best_partner(student, partners):
    best_match = []
    student_interests = {student[1], student[2], student[3]}
    for partner in partners:
        partner_interests = {partner[1], partner[2], partner[3]}
        common_interest = student_interests.intersection(partner_interests)
        best_match.append((len(common_interest), partner[0]))
    best_match.sort(reverse= True)
    print(best_match)
    return best_match[0][1]


student = ['Albert', 'football', 'chess', 'dungeons and dragons']
partners = [['Beatrice', 'hockey', 'football', 'scouting'],
['Charles', 'chess', 'history', 'football'],
['Danielle', 'polo', 'hunting', 'dungeons and dragons']]

print(best_partner(student, partners))
