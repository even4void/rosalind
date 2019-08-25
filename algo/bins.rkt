#lang racket

(define (bins lst start end elt)
  (let ([mid (floor (+ start end))])
    (cond [(> start end) -1]
          [(= elt (list-ref lst mid)) (add1 mid)]
          [(< elt (list-ref lst mid)) (bins lst start (sub1 mid) elt)]
          [else (bins lst (add1 mid) end elt)])))

(define array '(10 20 30 40 50))
(define idx '(40 10 35 15 40 20))

(for/list ([x idx]) (bins array 0 (sub1 (length array)) x))
