# Footnotes

Some of the optimizations in the bsim4.py model were hand done

## While loop unrolling

An iterative while loop (bounded by iterations = 4) was hand expanded into the function body x4

## For loop vectorization

A for loop bounded by nf in bsim4.py was vectorized using jnp (jax numpy) to remove the loop structure

## BSIM4 VA bug fixes

Original BSIM4 VA had bugs  
For more information view code/OpenVAF-altered/OpenVAF/integration_tests/BSIM4/bsim4_origin.md