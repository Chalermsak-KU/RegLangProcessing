echo import unittest
echo from contextlib import redirect_stdout
echo from reglang.$2 import $2
echo
echo class Test"$1(unittest.TestCase):"
echo
for f in test"$1"*.py
do
    awk -f makeunittest.awk `basename $f .py`
    echo
done

echo "if __name__ == '__main__':"
echo "    unittest.main()"
