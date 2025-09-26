const { Cliente, Cuenta, Fintech } = require('../modelo.js');

describe('Cliente', () => {
    it('debería crear un cliente con datos válidos', () => {
        const cliente = new Cliente(1, 'Juan', 'Perez', '12345678', 'juan@test.com', 'password123', 'password123');
        expect(cliente).toBeInstanceOf(Cliente);
        expect(cliente.id).toBe(1);
        expect(cliente.email).toBe('juan@test.com');
    });

    it('debería lanzar un error si el email es inválido', () => {
        expect(() => {
            new Cliente(1, 'Juan', 'Perez', '12345678', 'email-invalido', 'password123', 'password123');
        }).toThrow('Email inválido');
    });

    it('debería lanzar un error si la contraseña es muy corta', () => {
        expect(() => {
            new Cliente(1, 'Juan', 'Perez', '12345678', 'juan@test.com', '123', '123');
        }).toThrow('Password inválido');
    });

    it('debería lanzar un error si las contraseñas no coinciden en la creación', () => {
        expect(() => {
            new Cliente(1, 'Juan', 'Perez', '12345678', 'juan@test.com', 'password123', 'password456');
        }).toThrow('Las contraseñas no coinciden');
    });

    it('debería actualizar la contraseña correctamente', () => {
        const cliente = new Cliente(1, 'Juan', 'Perez', '12345678', 'juan@test.com', 'password123', 'password123');
        cliente.actualizarPassword('nuevaPassword456', 'nuevaPassword456');
        expect(cliente.password).toBe('nuevaPassword456');
    });

    it('debería lanzar un error al actualizar si las contraseñas no coinciden', () => {
        const cliente = new Cliente(1, 'Juan', 'Perez', '12345678', 'juan@test.com', 'password123', 'password123');
        expect(() => {
            cliente.actualizarPassword('nuevaPassword456', 'diferente');
        }).toThrow('Las contraseñas no coinciden');
    });
});

describe('Cuenta', () => {
    let cliente;
    let cuenta;

    beforeEach(() => {
        cliente = new Cliente(1, 'Ana', 'Gomez', '87654321', 'ana@test.com', 'password123', 'password123');
        cuenta = new Cuenta('ACC1', cliente, 1000);
    });

    it('debería depositar dinero y actualizar el saldo', () => {
        cuenta.depositar(500, 'Abono de sueldo');
        expect(cuenta.consultarSaldo()).toBe(1500);
        expect(cuenta.movimientos.length).toBe(1);
        expect(cuenta.movimientos[0].tipo).toBe('Depósito');
        expect(cuenta.movimientos[0].monto).toBe(500);
    });

    it('debería retirar dinero y actualizar el saldo', () => {
        cuenta.retirar(200, 'Compra online');
        expect(cuenta.consultarSaldo()).toBe(800);
        expect(cuenta.movimientos.length).toBe(1);
        expect(cuenta.movimientos[0].tipo).toBe('Retiro');
    });

    it('debería lanzar un error al retirar si el saldo es insuficiente', () => {
        expect(() => {
            cuenta.retirar(1500, 'Intento de sobregiro');
        }).toThrow('Saldo insuficiente');
        expect(cuenta.consultarSaldo()).toBe(1000); // El saldo no debe cambiar
    });
});

describe('Fintech', () => {
    let fintech;

    beforeEach(() => {
        fintech = new Fintech();
    });

    it('debería crear un cliente y su cuenta asociada', () => {
        const cliente = fintech.crearCliente('Carlos', 'carlos@test.com', 'pass123456', 'pass123456');
        expect(cliente).toBeInstanceOf(Cliente);
        expect(fintech.clientes.size).toBe(1);
        expect(fintech.cuentas.size).toBe(1);

        const cuenta = fintech.obtenerCuentaPorCliente(cliente.id);
        expect(cuenta).toBeDefined();
        expect(cuenta.cliente.id).toBe(cliente.id);
    });

    it('debería lanzar un error si el email del cliente ya existe', () => {
        fintech.crearCliente('Carlos', 'carlos@test.com', 'pass123456', 'pass123456');
        expect(() => {
            fintech.crearCliente('Otro Carlos', 'carlos@test.com', 'otraPass', 'otraPass');
        }).toThrow('Ya existe un cliente con el correo electrónico carlos@test.com.');
    });

    it('debería permitir el login de un usuario válido', () => {
        fintech.crearCliente('Lucia', 'lucia@test.com', 'luciapass', 'luciapass');
        const clienteLogueado = fintech.login('lucia@test.com', 'luciapass');
        expect(clienteLogueado).toBeDefined();
        expect(clienteLogueado.email).toBe('lucia@test.com');
        expect(fintech.cuentaActual).toBeDefined();
    });

    it('debería lanzar un error con credenciales de login incorrectas', () => {
        fintech.crearCliente('Lucia', 'lucia@test.com', 'luciapass', 'luciapass');
        expect(() => {
            fintech.login('lucia@test.com', 'pass-incorrecta');
        }).toThrow('Correo electrónico o contraseña incorrectos.');
    });

    it('debería realizar una transferencia entre dos cuentas', () => {
        const clienteOrigen = fintech.crearCliente('Maria', 'maria@test.com', 'pass123', 'pass123');
        const clienteDestino = fintech.crearCliente('Pedro', 'pedro@test.com', 'pass456', 'pass456');

        const cuentaOrigen = fintech.obtenerCuentaPorCliente(clienteOrigen.id);
        const cuentaDestino = fintech.obtenerCuentaPorCliente(clienteDestino.id);

        // Depositar fondos en la cuenta de origen para la prueba
        fintech.depositar(cuentaOrigen.codigo, 1000);
        expect(fintech.consultarSaldo(cuentaOrigen.codigo)).toBe(1000);

        fintech.transferir(cuentaOrigen.codigo, 'pedro@test.com', 300, 'Regalo');

        expect(fintech.consultarSaldo(cuentaOrigen.codigo)).toBe(700);
        expect(fintech.consultarSaldo(cuentaDestino.codigo)).toBe(300);

        const movimientosOrigen = fintech.obtenerMovimientos(cuentaOrigen.codigo);
        expect(movimientosOrigen.length).toBe(2); // Depósito inicial y retiro de transferencia
        expect(movimientosOrigen[1].motivo).toContain('Transferencia a');

        const movimientosDestino = fintech.obtenerMovimientos(cuentaDestino.codigo);
        expect(movimientosDestino.length).toBe(1); // Depósito de transferencia
        expect(movimientosDestino[0].motivo).toContain('Transferencia de');
    });

    it('debería lanzar un error al transferir con saldo insuficiente', () => {
        const clienteOrigen = fintech.crearCliente('Maria', 'maria@test.com', 'pass123', 'pass123');
        fintech.crearCliente('Pedro', 'pedro@test.com', 'pass456', 'pass456');
        const cuentaOrigen = fintech.obtenerCuentaPorCliente(clienteOrigen.id);

        fintech.depositar(cuentaOrigen.codigo, 100);

        expect(() => {
            fintech.transferir(cuentaOrigen.codigo, 'pedro@test.com', 200, 'Intento fallido');
        }).toThrow('Saldo insuficiente en la cuenta origen.');
    });
});