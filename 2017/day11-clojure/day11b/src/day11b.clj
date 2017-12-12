(ns day11b
  (:require [clojure.string :as str]))



(defn abs "(abs n) is the absolute value of n" [n]
(cond
(not (number? n)) (throw (IllegalArgumentException.
                            "abs requires a number"))
(neg? n) (- n)
:else n))


(defn calc [arr]

    (def f (frequencies arr))

    (def s (or (get f "s") 0))
    (def n (or (get f "n") 0))
    (def se (or (get f "se") 0))
    (def sw (or (get f "sw") 0))
    (def ne (or (get f "ne") 0))
    (def nw (or (get f "nw") 0))

    ;;{"s" 1342, "nw" 1071, "sw" 1372, "ne" 1628, "se" 1511, "n" 1299}

    ;;{"s" 1342, "nw" 1071, "sw" 1372, "ne" 1628, "se" 1511, "n" 1299}
    ;;"s" 43 "se" 440 "ne" 256
    ;;"se" 440+43 "ne" 256-43
    ;;"se" 483 "ne" 213
    ;;696

    ;;a0=0
    ;;b0=0

    ;;a1=s-n -(ne+nw)= 
    ;;b1=ne+se-sw-nw=(ne + se) - (sw + nw)


    (def x (- (+ n ne) (+ s sw)))
    (def y (- (+ se ne) (+ nw sw)))

    ;;if( condition
    ;;value-if-true
    ;;value-if-false)

    (defn not-negative? [n1 n2]
        (if (<= 0 (* x y)) true false))

    (def dist (if(not-negative? x y) (max (abs x) (abs y)) (+ (abs x) (abs y)))) 

    dist
    )



(defn -main []

    (def line (slurp "day11.input"))
    ;;(def line "ne,ne,ne")
    (require '[clojure.string :as str])

    (def arr (str/split line #","))


    (def max (calc arr))

    (def a (atom (count arr)))    
    (while (pos? @a) (do 
        (def arr (drop-last arr))
        (def dist (calc arr))    
        (def max (if (> dist max) dist max))
        (println "current max is: " max)
        (swap! a dec)        
        ))

    (println "answer is: " max))


