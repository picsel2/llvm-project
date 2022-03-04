# Check that failed tests are saved with negative test time to indicate failure

# RUN: not %{lit} %{inputs}/save-failed
# RUN: FileCheck %s < %{inputs}/save-failed/.lit_test_times.txt

# CHECK-DAG: {{^[^-].*}} pass.txt
# CHECK-DAG: {{^-.*}} fail.txt
