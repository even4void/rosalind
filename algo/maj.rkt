#lang racket

(define (counter x lst)
  (if (null? lst) 0
      (if (= x (car lst))
          (+ 1 (counter x (cdr lst)))
          (counter x (cdr lst)))))

(define items (list 8 7 7 7 1 7 3 7))
(apply max (for/list ([i (remove-duplicates items)]) (counter i items)))
