# Verilog-A to Python Pipeline

This runs the OpenVAF path:

```text
Verilog-A -> HIR -> MIR -> LIR -> Python
```

The key flag is:

```bash
--backend mir-lift
```

Without that flag, OpenVAF uses the normal LLVM/OSDI path instead of producing Python.

## 1. Set LLVM

If LLVM 15.0.7 is installed under `/opt/LLVM`, run:

```bash
export LLVM_CONFIG=/opt/LLVM/bin/llvm-config
```

Verify:

```bash
$LLVM_CONFIG --version
```

Expected:

```text
15.0.7
```

## 2. Go To OpenVAF

Run these commands from the repository root:

```bash
REPO_ROOT=$(pwd)
cd code/OpenVAF-altered/OpenVAF
```

## 3. Build OpenVAF

You only need to rebuild if the binary is missing, source code changed, `target/` was deleted, or you ran `cargo clean`.

```bash
cargo build -p openvaf-driver --bin openvaf-r
```

From the repository root, the binary will be:

```text
code/OpenVAF-altered/OpenVAF/target/debug/openvaf-r
```

## 4. Smoke Test With DIODE

This is the small/fast test.

```bash
./target/debug/openvaf-r \
  integration_tests/DIODE/diode.va \
  --backend mir-lift \
  --dump-lir \
  -o "$REPO_ROOT/diode.py"
```

Check output:

```bash
ls -lh "$REPO_ROOT/diode.py"
sed -n '1,80p' "$REPO_ROOT/diode.py"
```

## 5. Run BSIM4

This is the large model.

```bash
./target/debug/openvaf-r \
  integration_tests/BSIM4/bsim4.va \
  --backend mir-lift \
  --dump-lir \
  -o "$REPO_ROOT/bsim4.py"
```

Check output:

```bash
ls -lh "$REPO_ROOT/bsim4.py"
sed -n '1,80p' "$REPO_ROOT/bsim4.py"
```

## 6. Optional: Output To `/tmp`

Use `/tmp` for disposable output:

```bash
./target/debug/openvaf-r \
  integration_tests/BSIM4/bsim4.va \
  --backend mir-lift \
  --dump-lir \
  -o /tmp/bsim4.py
```

View it:

```bash
ls -lh /tmp/bsim4.py
sed -n '1,80p' /tmp/bsim4.py
```

Files in `/tmp` may be removed after reboot or cleanup.

## Notes

- You do not need ngspice for this Python pipeline.
- You do need ngspice for running `.osdi` models in circuit simulations.
- Building `openvaf-r` is not per terminal. Once built, the binary stays in `target/debug/openvaf-r`.
- `LLVM_CONFIG` is mainly needed while building OpenVAF.
