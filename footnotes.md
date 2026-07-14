# Footnotes

Some of the optimizations in the bsim4.py model were hand done

## While loop unrolling

An iterative while loop (bounded by iterations = 4) was hand expanded into the function body x4

## For loop vectorization

A for loop bounded by nf in bsim4.py was vectorized using jnp (jax numpy) to remove the loop structure