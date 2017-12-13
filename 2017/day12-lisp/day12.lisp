(load "~/quicklisp/setup.lisp")
(ql:quickload :cl-strings)

(defun get-file (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

;;plist of all pipes from input 
(defvar *pipes* nil)
;;list of all traversed ids
(defvar *traversed* ())


(defun make-pipe (id ids)
  (list :id id :ids ids))

(defun add-pipe (pipe) (push pipe *pipes*))


;;reading input into list of lines
(defparameter *lines* (get-file "day12.input"))

;;(prin1 *lines*)

;;parsing list of lines into plist of :id and connected :ids
(dolist (x *lines*) 
    (defparameter *id*  (nth 0 (cl-strings:split x " <-> ")))
    (defparameter *ids*  (nth 1 (cl-strings:split x " <-> ")))

    (add-pipe (make-pipe *id* *ids*))


        )

(print *pipes*)
(print "pipes printed")
(print " ")


(defun select-by-id (id)
  (remove-if-not
   #'(lambda (pipe) (equal (getf pipe :id) id))
   *pipes*))


(defun traverse (id)
    ;;mark this id as traversed
    (print ">>>>>>>>>>>>")
    (push id *traversed*)

    (defparameter *pipe* (nth 0 (select-by-id id)))
    (defparameter *ids*  (getf *pipe* :ids))    

    ;;split into list of ids to traverse next
    (defparameter *nextids*  (cl-strings:split *ids* ", "))

    (print "id references")
    (print id)
    (print *ids*)
    (print *nextids*)
    (print *pipe*)
    (print *traversed*)

    (dolist (x *nextids*) 
        (print "iterating nextids")
        (print x)

        (print (member x *traversed*))
        ;;check if this id was already traversed

        ;;(find "124" *traversed* :test #'equal)

        (if (not (find x *traversed*  :test #'equal))
                    (traverse x)
                    (print "traverse next")
        )


    )


)

(traverse "0")

;;(print (find "1" '(4 "1" "2" 3)))

(print *traversed*)
(print "answer is: ")
(print (length *traversed*))