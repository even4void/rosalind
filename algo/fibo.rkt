#lang typed/racket

;; A little attempt at memoization in Racket. A more interesting discussion
;; is provided at https://blog.jverkamp.com/2012/10/20/memoization-in-racket.
;; Another implementation is available on Henry Brooks website:
;; https://hebr3.github.io/2017/04/memoization-in-racket.html.
;; There's also a crazy version on Coursera (start at 3'50):
;; https://www.coursera.org/lecture/programming-languages-part-b/memoization-SqEc5.
;;
;; Even better, there's a package for that: https://docs.racket-lang.org/memoize,
;; or (t)yped memoize.
;;
;; Finally, there is a nice discussion of memoization, from which most the code
;; below borrows from, on the Racket blog: Dynamic Programming versus Memoization,
;; https://blog.racket-lang.org/2012/08/dynamic-programming-versus-memoization.html.
;;
;; Note that the _fast doubling algorithm_ is available in my Euler repo:
;; https://github.com/even4void/euler/blob/master/002.rkt

(require tmemoize)

(: fib (-> Integer Integer))
(define fib (memoize (lambda ([n : Integer])
                        (if (<= n 2) 1
                            (+ (fib (- n 1))
                               (fib (- n 2)))))))

(displayln (fib 23))
