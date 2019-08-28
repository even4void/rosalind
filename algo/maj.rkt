#lang racket

(define (counter lst #:item x)
  (if (null? lst) 0
      (if (= x (car lst))
          (+ 1 (counter (cdr lst) x))
          (counter (cdr lst) x))))

(define items (list 8 7 7 7 1 7 3 7))
(apply counter items #:item (remove-duplicates items))
