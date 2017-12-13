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
(defvar *leftovers* ())


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
    (push *id* *leftovers*)


        )

(print *pipes*)
(print "pipes printed")
(print " ")


(defun select-by-id (id)
  (remove-if-not
   #'(lambda (pipe) (equal (getf pipe :id) id))
   *pipes*))

(defun remove-it (it list)
  (if (null list) 0
      (if (= it (car list))
          (delete (car list))
          (remove-it (cdr list)))))

(defun traverse (id)
    ;;mark this id as traversed
    ;;(print ">>>>>>>>>>>>")
    (push id *traversed*)
    (setf *leftovers* (delete id *leftovers* :test #'equal))


    (defparameter *pipe* (nth 0 (select-by-id id)))
    (defparameter *ids*  (getf *pipe* :ids))    

    ;;split into list of ids to traverse next
    (defparameter *nextids*  (cl-strings:split *ids* ", "))

    ;;(print "id references")
    ;;(print id)
    ;;(print *ids*)
    ;;(print *nextids*)
    ;;(print *pipe*)
    ;;(print *traversed*)

    (dolist (x *nextids*) 
        ;;(print "iterating nextids")
        ;;(print x)

        ;;(print (member x *traversed*))
        ;;check if this id was already traversed

        ;;(find "124" *traversed* :test #'equal)

        (if (not (find x *traversed*  :test #'equal))
                    (traverse x)
                    ;;(print "traverse next")
        )


    )


)


(defparameter *sum* 0)
(defparameter *count* 0)

;;(print *leftovers*)
;;(print (length *leftovers*))
;;(print (length *pipes*))



    (loop 
        (if (= (length *leftovers*) 0) (return))
        (print "looping")

        (defparameter x (nth 0 *leftovers*))

        (defparameter *traversed* ())
        (print "finding groups")
        (print x)
        (traverse x)
        (setf *count* (+ *count* 1))
        (setf *sum* (+ *sum* (length *traversed*)))
        ;;(print *sum*)
        (print *traversed*)
        (print (length *traversed*))
        (print *leftovers*)
        (print (length *leftovers*))        
    )  





;;(print *traversed*)
;;(print *leftovers*)
(print "answer is: ")
;;(print *sum*)
(print *count*)


