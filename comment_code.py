##### INSTRUCTIONS FOR USE ######
# https://docs.google.com/document/d/1U3SQuMF9YfmDpFIt428f1Ep0cFHOwLDLP1W9jSh9PAo/edit



# All the possible spreadsheet column headers
headings = ['student name', 'class', 'semester grade',
            'key test', 'key test grade', 'average grade', 
            'essay excerpt 1', 'essay excerpt 2', 
            'skill 1', 'skill 2', 'skill 3', 
            'learning indicator 1', 'learning indicator 2', 'learning indicator 3', 
            'area of improvement 1', 'area of improvement 2', 'area of improvement 3'] 




import csv
def read_comment_notes(file_name:str):
    ''' reads the csv file of the teacher's spreadsheet and sorts the data to match the order of the headings in the headings list '''
    with open(file_name) as f:
        teacher_headings = [h.strip().lower() for h in next(f).split(',')]
        
        data = [row for row in csv.reader(f)]
    master = []
    for row in data:
        student = ['' for i in range(len(headings))]
        for i in range(len(row)):
            index = headings.index(teacher_headings[i])
            student[index] = row[i]
        master.append(student)

    return master


def read_class_descrip(file_name:str):
    ''' reads the separate class descriptions file '''
    class_descrips = []
    with open(file_name) as f:
        class_names = [name.strip().lower() for name in next(f).split(',')]
        class_descrips = [row for row in csv.reader(f)]
    return class_names, class_descrips[0]



def paragraph1(student_info, class_names, class_descrips):
    '''Paragraph 1: Class description/intro '''
    class_name = student_info[1]
    class_description = class_descrips[class_names.index(class_name.lower())]
    paragraph = f'This semester in {class_name}, {class_description}'
    return paragraph


def paragraph2(student_info):
    '''Paragraph 2: Positive attributes, student work/scores (if higher than B), learning indicators, skills '''
    name = student_info[0]
    key_test = student_info[3]
    key_test_score = student_info[4]
    average_grade = student_info[5]
    essay_excerpt_1 = student_info[6]
    essay_excerpt_2 = student_info[7]
    skill_1 = student_info[8]
    skill_2 = student_info[9]
    skill_3 = student_info[10]
    learning_indicator_1 = student_info[11]
    learning_indicator_2 = student_info[12]
    learning_indicator_3 = student_info[13]
    comment = [f'You have been doing well this semester, {name}.']
    if key_test_score and key_test:
        s1 = f'On one of our most important tests, the {key_test}, you scored a {key_test_score}.'
        comment.append(s1)
    if average_grade:
        s2 = f'Over the course of this semester you scored a {average_grade} on average.'
        comment.append(s2)
    if skill_1 and skill_2 and skill_3:
        s5 = f'Your primary strengths this year were: {skill_1}, {skill_2}, {skill3}.'
        comment.append(s5)
    if skill_1 and skill_2:
        s6 = f'Your primary strengths this year were: {skill_1} and {skill_2}.'
        comment.append(s6)
    if skill_1 or skill_2 or skill_3:
        s7 = f'Your primary strength this year was {skill_1}.'
        comment.append(s7)
    if essay_excerpt_1:
        if essay_excerpt_1[0] != '"':
            s3 = f'Your skills were reflected in your writing, which can be seen in one of your pieces you wrote, "{essay_excerpt_1}".'
            comment.append(s3)
        else:
            s3 = f'Your skills were reflected in your writing, for example when you wrote, {essay_excerpt_1}.'
            comment.append(s3)
        if essay_excerpt_2:
            s4 = f'You also wrote, {essay_excerpt_2}.'
            comment.append(s4)
    if learning_indicator_1:
        s8 = f'One of our learning indicators was: {learning_indicator_1}.'
        comment.append(s8)
    if learning_indicator_2:
        s9 = f'We focused on {learning_indicator_2}.'
        comment.append(s9)
    if learning_indicator_3:
        s10 = f'We valued {learning_indicator_3}.'
        comment.append(s10)
    paragraph = ' '.join(comment)
    return paragraph


def paragraph3(student_info):
    '''Paragraph 3: Areas of improvement, student work/scores (if lower than B)'''
    name = student_info[0]
    a1 = student_info[14]
    a2 = student_info[15]
    a3 = student_info[16]
    if a1:
        p = f'Try focusing on {a1}.'
    if a1 and a2:
        p = f'Try focusing on {a1} and {a2}.'
    if a1 and a2 and a3:
        p = f'Try focusing on {a1}, {a2}, and {a3}.'
    paragraph = f'{name}, while this semester has been bright, there are some improvements you could make. {p}'
    return paragraph

def paragraph4(student_info):
    '''Paragraph 4: Conclusion, semester grade'''
    name = student_info[0]
    semester_grade = student_info[2]
    paragraph = f'Overall {name}, you ended the semester with a {semester_grade}. I greatly enjoyed the experience of teaching you and I felt you lit up the class with your mind and personality. I look forward to seeing you again another semester or in a different class.'
    return paragraph


def check_grammar(comment, student_name):
    ''' makes sure articles and capitalization is correct '''
    comment = comment.strip()
    ec = []
    for i in range(len(comment)):
        if i == 0:
            ec.append(comment[0].upper())
        elif comment[i-1] == ' ' and comment[i-2] in '.?!':
            ec.append(comment[i].upper())
        elif comment[i:i+len(student_name)].lower() == student_name.lower():
            ec.append(comment[i].upper())
        elif comment[i] == 'a' and comment[i+1] == ' ' and comment[i+2].lower() in '8aef' and comment[i+3] in '0123456789+-.!? ':
            ec.append('an')
        else:
            ec.append(comment[i]) 
    return ''.join(ec)


def write_files(comments):
    ''' writes each student's comment to a it's own file with the student's name as it's name '''
    for data in comments:
        student = data[0]
        comment = data[1]
        with open(f'{student}.txt', 'w') as f:
            f.write(comment)





def main(file_name, classD_file_name, headings):
    ''' makes each paragraph, compiles them into one comment, and writes to files. '''
    master = read_comment_notes(file_name)
    class_names, class_descrips = read_class_descrip(classD_file_name)
    comments = []
    for student_number in range(len(master)):
        p1 = paragraph1(master[student_number], class_names, class_descrips) + '\n\n'
        p2 = paragraph2(master[student_number]) + '\n\n'
        p3 = paragraph3(master[student_number]) + '\n\n'
        p4 = paragraph4(master[student_number])
        comment = p1+p2+p3+p4
        comment = check_grammar(comment, master[student_number][0]) # Check for punctuation, articles, capitalization, etc.
        comments.append([master[student_number][0], comment]) # master[0] = student name
    write_files(comments)


# Runs code
main('tcp.csv', 'tcpClass.csv', headings)
