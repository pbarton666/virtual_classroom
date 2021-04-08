# This builds on the linux/conda/python box and adds Jupyter Notebook
#   server on port 8888.

#Build with $docker build -f "./Dockerfile" -t student .
#Run 
# $docker run -it student    # interactive mode logged in as student
# $docker run -p 7000:8888   # server mode: '7000' can be any unallocated port on client
FROM localconda39

USER root

WORKDIR /home
RUN useradd -ms /bin/bash student
RUN echo 'student:student' | chpasswd
RUN echo 'root:root' | chpasswd 
RUN adduser student sudo

RUN chmod -R +x /home/student

USER student
WORKDIR /home/student/src/course_files
COPY . /home/student/src/course_files
#RUN git clone https://github.com/pbarton666/learninglab #/home/student/src/course_files

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]