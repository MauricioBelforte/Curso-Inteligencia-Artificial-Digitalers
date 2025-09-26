class Cliente {
    // Atributos privados de la clase
    #password;

    constructor(id, nombre, apellido, dni, email, password, confirmPassword) {
        if (!this.validarNombre(nombre)) throw new Error('Nombre inválido');
        if (!this.validarEmail(email)) throw new Error('Email inválido');
        if (!this.validarPassword(password)) throw new Error('Password inválido');
        if (password !== confirmPassword) throw new Error('Las contraseñas no coinciden');

        this.id = id;
        this.nombre = nombre; // El this.nombre llama al setter de nombre
        this.apellido = apellido; // Llama al setter de apellido
        this.dni = dni; // Llama al setter de dni
        this.email = email; // Llama al setter de email
        this.#password = password;
    }

    // Getters y setters con propiedades internas privadas o protegidas 

    get nombre() {
        return this._nombre;
    }

    set nombre(nuevoNombre) {
        if (!this.validarNombre(nuevoNombre)) throw new Error('Nombre inválido');
        this._nombre = nuevoNombre;
    }


    get apellido() {
        return this._apellido;
    }

    set apellido(apellido) {
        // Podrías añadir una validación similar a la del nombre si lo necesitas
        this._apellido = apellido;
    }


    get dni() {
        return this._dni;
    }

    set dni(dni) {
        // Podrías añadir una validación para el DNI aquí
        this._dni = dni;
    }


    get email() {
        return this._email;
    }

    set email(email) {
        if (!this.validarEmail(email)) throw new Error('Email inválido');
        this._email = email;
    }


    get password() {
        return this.#password;
    }

    set password(password) {
        this.#password = password;
    }

    actualizarPassword(nuevaPassword, confirmarPassword) {
        if (!this.validarPassword(nuevaPassword)) throw new Error('Password inválido');
        if (nuevaPassword !== confirmarPassword) throw new Error('Las contraseñas no coinciden');
        this.#password = nuevaPassword;
    }

    // Validar el nombre
    validarNombre(nombre) {
        return typeof nombre === 'string' && nombre.trim().length > 0;
    }

    // Validar el correo electrónico
    validarEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Validar la contraseña
    validarPassword(password) {
        return typeof password === 'string' && password.length >= 6;
    }
}

class Movimiento {
    constructor(tipo, monto, fecha, motivo) {
        this.tipo = tipo; // 'Depósito' o 'Retiro'
        this.monto = monto;
        this.fecha = fecha;
        this.motivo = motivo;
    }
}


class Cuenta {
    constructor(codigo, cliente, saldoInicial = 0) {
        this.codigo = codigo; // Código único
        this.cliente = cliente; // Referencia al objeto Cliente
        this.saldo = saldoInicial;
        this.movimientos = []; // Lista de movimientos
    }

    // Método para depositar dinero
    depositar(monto, motivo) {
        this.saldo += monto;
        this.registrarMovimiento('Depósito', monto, motivo);
    }



    // Método para retirar dinero
    retirar(monto, motivo) {
        if (monto > this.saldo) {
            throw new Error('Saldo insuficiente');
        }
        this.saldo -= monto;
        this.registrarMovimiento('Retiro', monto, motivo);
    }

    // Método para registrar un movimiento
    registrarMovimiento(tipo, monto, motivo) {
        const movimiento = new Movimiento(tipo, monto, new Date(), motivo);
        this.movimientos.push(movimiento);
    }

    // Método para consultar el saldo
    consultarSaldo() {
        return this.saldo;
    }
}

class Fintech {
    constructor() {
        this.clientes = new Map(); // Almacenar clientes usando un Map para búsquedas rápidas
        this.cuentas = new Map();  // Almacenar cuentas usando un Map para búsquedas rápidas
        this.clienteIdCounter = 1; // Contador para generar IDs únicos
        this.cuentaCodigoCounter = 1; // Contador para generar códigos únicos
        this.cuentaActual = null;
    }


    // Método para crear un nuevo cliente
    crearCliente(nombre, email, password, confirmPassword) {
        // Verificar si ya existe un cliente con el mismo email (ignorando mayúsculas/minúsculas)
        for (let cliente of this.clientes.values()) {
            if (cliente.email.toLowerCase() === email.toLowerCase()) {
                throw new Error(`Ya existe un cliente con el correo electrónico ${email}.`);
            }
        }

        const id = this.clienteIdCounter++;
        // Crear el nuevo cliente
        const nuevoCliente = new Cliente(id, nombre, '', '', email, password, confirmPassword);
        this.clientes.set(id, nuevoCliente);

        // Crear una cuenta asociada al nuevo cliente usando crearCuenta
        this.crearCuenta(id);

        return nuevoCliente;
    }

    // Método para crear una nueva cuenta
    crearCuenta(clienteId, saldoInicial = 0) {
        const cliente = this.clientes.get(clienteId);
        if (!cliente) {
            throw new Error(`Cliente con ID ${clienteId} no encontrado.`);
        }
        const codigo = `ACC${this.cuentaCodigoCounter++}`;
        const nuevaCuenta = new Cuenta(codigo, cliente, saldoInicial);
        this.cuentas.set(codigo, nuevaCuenta);
        return nuevaCuenta;
    }

    // Método para realizar un depósito
    depositar(codigoCuenta, monto) {
        const cuenta = this.cuentas.get(codigoCuenta);
        if (!cuenta) {
            throw new Error(`Cuenta con código ${codigoCuenta} no encontrada.`);
        }
        cuenta.depositar(monto);
    }

    // Método para realizar un retiro
    retirar(codigoCuenta, monto) {
        const cuenta = this.cuentas.get(codigoCuenta);
        if (!cuenta) {
            throw new Error(`Cuenta con código ${codigoCuenta} no encontrada.`);
        }
        cuenta.retirar(monto);
    }

    // Método para consultar el saldo de una cuenta
    consultarSaldo(codigoCuenta) {
        const cuenta = this.cuentas.get(codigoCuenta);
        if (!cuenta) {
            throw new Error(`Cuenta con código ${codigoCuenta} no encontrada.`);
        }
        return cuenta.consultarSaldo();
    }

    // Método para obtener el historial de movimientos de una cuenta
    obtenerMovimientos(codigoCuenta) {
        const cuenta = this.cuentas.get(codigoCuenta);
        if (!cuenta) {
            throw new Error(`Cuenta con código ${codigoCuenta} no encontrada.`);
        }
        return cuenta.movimientos;
    }

    login(email, password) {
        for (let cliente of this.clientes.values()) {
            if (cliente.email === email && cliente.password === password) {
                this.cuentaActual = this.obtenerCuentaPorCliente(cliente.id);
                return cliente; // Devuelve el objeto Cliente si las credenciales son correctas
            }
        }
        throw new Error('Correo electrónico o contraseña incorrectos.');
    }

    obtenerCuentaPorCliente(clienteId) {
        for (let cuenta of this.cuentas.values()) {
            if (cuenta.cliente.id === clienteId) {
                return cuenta; // Devuelve el objeto Cuenta si se encuentra una cuenta asociada al cliente
            }
        }
        throw new Error(`No se encontró ninguna cuenta para el cliente con ID ${clienteId}.`);
    }

    transferir(codigoCuentaOrigen, emailDestino, monto, motivo) {
        const cuentaOrigen = this.cuentas.get(codigoCuentaOrigen);
        if (!cuentaOrigen) {
            throw new Error(`Cuenta origen con código ${codigoCuentaOrigen} no encontrada.`);
        }

        let cuentaDestino = null;
        for (let cliente of this.clientes.values()) {
            if (cliente.email === emailDestino) {
                cuentaDestino = this.obtenerCuentaPorCliente(cliente.id);
                break;
            }
        }

        if (!cuentaDestino) {
            throw new Error(`No se encontró ninguna cuenta asociada al correo ${emailDestino}.`);
        }

        if (cuentaOrigen.saldo < monto) {
            throw new Error('Saldo insuficiente en la cuenta origen.');
        }

        cuentaOrigen.retirar(monto, `Transferencia a ${cuentaDestino.codigo}: ${motivo}`);
        cuentaDestino.depositar(monto, `Transferencia de ${codigoCuentaOrigen}: ${motivo}`);
    }
}

// Si el código se ejecuta en un navegador, exporta la instancia a window.
if (typeof window !== 'undefined') {
    window.modelo = new Fintech();
}

// Exporta las clases para poder usarlas en otros módulos (como los tests con Jest)
module.exports = { Cliente, Cuenta, Fintech, Movimiento };