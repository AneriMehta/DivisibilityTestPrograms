<?php

function testFor3($value)
{
    return is_numeric($value) && ($value / 3 == floor($value / 3));
}