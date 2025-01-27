(c-declare #<<c-declare-end
  int f(int n) {
      return n * n + 2 * n + 3;
  }
c-declare-end
)

(define f-scheme (c-lambda (int) int "f"))

(define arr '(106 117 84 121 119 83 90 52 54 20 15 205 201 163 151 118 70 52 52 230 211 135 125 29 0 206 178 124 20 242 162 103 28 255 164 124 60 153 204 125))

(display "Password: ")
(define input (read-line))

(define good 1)

(define len (string-length input))

(if (not (= len 40))
  (set! good 0)
)

(let loop ((i 0))
  (if (< i len)
      (begin
        (if (not (= (list-ref arr i)
                    (bitwise-xor 
                      (bitwise-and (f-scheme i) 255)
                      (char->integer (string-ref input i))
                    )
                  )
            )
            (begin
              (set! good 0)
              #f
            )
        )
        
        (if (= good 1)
            (loop (+ i 1)))
      )
      #t
  )
)

(if (= good 1)
    (display "Correct!\n")
    (display "Wrong!\n"))
