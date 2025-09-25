using NUnit.Framework;

namespace Logica.Tests {
    public class DivisionTests {

        [Test]
        public void DivisionCorrecta() {
            // NUnit usa Assert.That
            Assert.That(Division.Dividir(10, 2), Is.EqualTo(5));
        }

        [Test]
        public void DivisionPorCero() {
            Assert.Throws<System.DivideByZeroException>(() => Division.Dividir(10, 0));
        }
    }
}
