
class Handler(val x: Int, y: Int) {
	def Show(s: String) { println("%s: x: %d, y: %d\n".format(s, x, y)) }
	def Func(a: Int, b:Int, c:Int) = { a+b+c }
}

class Runner(val x: Int) {
	def inc() = { x+1 }
	def dec() = { x-1 }
	def sum(a:Int) = { x+a }
	def min(a:Int) = { x-a }
}

object Scratch extends App {
	println("Scratch ver. 0.1, args: %s\n".format(args(0)))

	private val r = new Runner(7)

	println("Runner.inc: %d".format(r.inc))
	println("Runner.dec: %d".format(r.dec))
	println("Runner.sum: %d".format(r.sum(3)))
	println("Runner.min: %d".format(r.min(11)))

	private val h = new Handler(4, 7)
	h.Show("Yessioor! ")
}

