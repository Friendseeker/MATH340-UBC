import shutil

from dirsync import sync
import os
if __name__ == '__main__':
    # Algorithm:
    # Loop through every folder in source
    # For each folder:
    #   read topics.txt
    #   compute the current path
    #   print the destination path
    #   invoke dirsync

    problems = set()
    topic_list = {'source'}
    source_dir = os.getcwd() + r'/practice_questions/source'

    for curr_dir, dirs, files in os.walk(source_dir):
        for file in files:
            if file == 'topics.txt':
                topic_path = os.path.join(curr_dir, file)
                with open(topic_path, 'r') as topic_file:
                    topics = topic_file.readlines()
                    for topic in topics:
                        topic = topic[:-1] if topic[-1] == '\n' else topic
                        problem_name = os.path.basename(curr_dir)

                        problems.add(problem_name)
                        topic_list.add(topic)

                        target_dir = os.getcwd() + f'/practice_questions/{topic}/{problem_name}'
                        sync(curr_dir, target_dir, 'sync', create=True)

    ## Remove problems that are not in the source
    practice_dir = os.getcwd() + '/practice_questions'
    for curr_dir, dirs, files in os.walk(practice_dir):
        path_name = os.path.basename(curr_dir)
        if path_name != 'practice_questions' and path_name not in topic_list and path_name not in problems:
            shutil.rmtree(curr_dir)

