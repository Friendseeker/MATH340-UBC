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
    source_dir = os.getcwd() + r'/practice_questions/source'
    for curr_dir, dirs, files in os.walk(source_dir):
        for file in files:
            if file == 'topics.txt':
                topic_path = os.path.join(curr_dir, file)
                with open(topic_path, 'r') as topic_file:
                    topics = topic_file.readlines()
                    for topic in topics:
                        topic = topic[:-1] # strip /n newline
                        problem_name = os.path.basename(curr_dir)
                        target_dir = os.getcwd() + f'/practice_questions/{topic}/{problem_name}'
                        sync(curr_dir, target_dir, 'sync', create=True)