import kotlin.math.*

fun main() {
    while (true) {
        println("Please choose an option:")
        println("1. Simple Calculator")
        println("2. Area Calculator")
        println("3. Advanced Calculator")
        println("4. Exit")
        val choice = readln().toInt()

        when (choice) {
            1 -> simpleCalculator()
            2 -> areaCalculator()
            3 -> advancedCalculator()
            4 -> {
                println("Exiting the program. Goodbye!")
                break
            }
            else -> println("Invalid choice. Please choose a valid option.")
        }
        println() // Print a blank line for better readability
    }
}

fun simpleCalculator() {
    print("Please enter the first number: ")
    val number1 = readln().toDouble()

    print("Please enter the second number: ")
    val number2 = readln().toDouble()

    print("Please enter one of the following operations: +,-,*,/: ")
    val operand = readln()

    val answer = when (operand) {
        "+" -> number1 + number2
        "-" -> number1 - number2
        "*" -> number1 * number2
        "/" -> {
            if (number2 != 0.0) number1 / number2
            else "You cannot divide by zero, do you want to try again?"
        }
        else -> "You did not choose a valid operation, please try again."
    }
    println("The answer is $answer")
}

fun areaCalculator() {
    println("Choose a shape to calculate the area:")
    println("1. Circle")
    println("2. Square")
    println("3. Rectangle")
    println("4. Triangle")

    val shapeChoice = readln().toInt()

    when (shapeChoice) {
        1 -> {
            print("Enter the radius of the circle: ")
            val radius = readln().toDouble()
            val area = Math.PI * radius * radius
            println("The area of the circle is $area")
        }
        2 -> {
            print("Enter the side length of the square: ")
            val side = readln().toDouble()
            val area = side * side
            println("The area of the square is $area")
        }
        3 -> {
            print("Enter the length of the rectangle: ")
            val length = readln().toDouble()
            print("Enter the width of the rectangle: ")
            val width = readln().toDouble()
            val area = length * width
            println("The area of the rectangle is $area")
        }
        4 -> {
            print("Enter the base of the triangle: ")
            val base = readln().toDouble()
            print("Enter the height of the triangle: ")
            val height = readln().toDouble()
            val area = 0.5 * base * height
            println("The area of the triangle is $area")
        }
        else -> {
            println("Invalid choice. Please restart and choose a valid option.")
        }
    }
}

fun advancedCalculator() {
    println("Choose an advanced operation:")
    println("1. Exponents")
    println("2. Square Roots")
    println("3. Show Factors of a Number")

    val advancedChoice = readln().toInt()

    when (advancedChoice) {
        1 -> {
            print("Enter the base value: ")
            val base = readln().toDouble()
            print("Enter the exponent value: ")
            val exponent = readln().toDouble()
            val result = base.pow(exponent)
            println("The result of $base raised to the power of $exponent is $result")
        }
        2 -> {
            print("Enter the value: ")
            val value = readln().toDouble()
            val result = sqrt(value)
            println("The square root of $value is $result")
        }
        3 -> {
            print("Enter the number to find its factors: ")
            val number = readln().toInt()
            val factors = findFactors(number)
            println("The factors of $number are: $factors")
        }
        else -> println("Invalid choice.")
    }
}

fun findFactors(number: Int): List<Int> {
    val factors = mutableListOf<Int>()
    for (i in 1..number) {
        if (number % i == 0) {
            factors.add(i)
        }
    }
    return factors
}
