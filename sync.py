import shutil
from pathlib import Path

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

    problems = dict()
    topic_list = set()
    source_dir = os.getcwd() + r'/practice_questions/source'

    for curr_dir, dirs, files in os.walk(source_dir):
        for file in files:
            if file == 'topics.txt':
                topic_path = os.path.join(curr_dir, file)
                with open(topic_path, 'r') as topic_file:
                    topics = topic_file.readlines()
                    problem_name = os.path.basename(curr_dir)

                    topics_without_newline = []
                    for topic in topics:
                        topic = topic[:-1] if topic[-1] == '\n' else topic
                        topics_without_newline.append(topic)
                        topic_list.add(topic)

                        target_dir = os.getcwd() + f'/practice_questions/{topic}/{problem_name}'
                        # sync(curr_dir, target_dir, 'sync', create=True)
                    problems[problem_name] = topics_without_newline

    ## Remove problems that are not in the source
    practice_dir = os.getcwd() + '/practice_questions'
    for curr_dir, dirs, files in os.walk(practice_dir):
        path_name = os.path.basename(curr_dir)
        topic_name = os.path.basename(Path(curr_dir).parent)

        whitelist = ['practice_questions', 'source', 'MATH340-UBC']

        # Do nothing when the curr_dir is in the whitelist
        if topic_name in whitelist:
            continue

        # If a topic folder is not one of the topics in source, delete the topic folder
        # Known bug: does not delete a topic folder with no sub-folders/files
        if topic_name not in topic_list:
            shutil.rmtree(Path(curr_dir).parent)

        # If a problem is misplaced (does not belong to current topic), remove the problem
        if topic_name not in problems[path_name]:
            shutil.rmtree(curr_dir)

    print(f'Successfully synced {len(problems)} problems!')
