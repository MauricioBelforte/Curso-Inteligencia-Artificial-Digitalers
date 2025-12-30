

-- ****************************************************
-- 2. CREACIÓN DE TABLAS (SIN RESTRICCIONES)
-- ****************************************************

-- TABLAS BASE Y GEOGRÁFICAS (Conjunto 1)
CREATE TABLE Provincia (
    Codigo_Provincia INT,
    Nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Localidad (
    Codigo_Postal VARCHAR(10),
    Nombre VARCHAR(100) NOT NULL,
    Codigo_Provincia INT NOT NULL
);

CREATE TABLE Cliente (
    CUIT VARCHAR(13),
    Razon_Social VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50),
    Codigo_Postal VARCHAR(10) NOT NULL
);

CREATE TABLE Lugar (
    Codigo_Lugar VARCHAR(10),
    Descripcion VARCHAR(100),
    Direccion VARCHAR(255),
    Codigo_Postal VARCHAR(10) NOT NULL
);

CREATE TABLE Puerto (
    Codigo_Puerto VARCHAR(10),
    Nombre VARCHAR(100) NOT NULL,
    Codigo_Postal VARCHAR(10) NOT NULL
);

CREATE TABLE Planta_Procesamiento (
    Nombre VARCHAR(100),
    Direccion VARCHAR(255) NOT NULL,
    Codigo_Postal VARCHAR(10) NOT NULL
);

CREATE TABLE Instalacion (
    Numero INT NOT NULL,
    Codigo_Planta VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50),
    Capacidad DECIMAL(10, 2)
);

CREATE TABLE Trabajador_de_Planta (
    Tipo_Doc VARCHAR(10) NOT NULL,
    Nro_Doc VARCHAR(20) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Rol VARCHAR(50),
    Codigo_Planta VARCHAR(100) NOT NULL
);

CREATE TABLE Producto_Derivado (
    CodProdDerivado VARCHAR(20),
    Precio DECIMAL(10, 2) NOT NULL,
    Clasificacion VARCHAR(50)
);

CREATE TABLE Especie (
    Codigo_Especie INT,
    Tipo VARCHAR(50),
    Nombre_Comun VARCHAR(100) NOT NULL,
    Nombre_Cientifico VARCHAR(100)
);

-- TABLAS DE TRANSPORTE Y CONTROL (Conjunto 1 y 2)
CREATE TABLE Camion (
    Patente VARCHAR(10),
    Marca VARCHAR(50) NOT NULL,
    Modelo VARCHAR(50),
    Capacidad DECIMAL(10, 2),
    Cargo VARCHAR(50)
);

CREATE TABLE Chofer (
    Tipo_Doc VARCHAR(10) NOT NULL,
    Nro_Doc VARCHAR(20) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20)
);

CREATE TABLE Traslado (
    Codigo_Traslado INT,
    Fecha DATE NOT NULL,
    Tipo VARCHAR(50),
    Patente VARCHAR(10) NOT NULL,
    Duracion INTERVAL,
    Codigo_Planta_Salida VARCHAR(100),
    Codigo_Planta_Llegada VARCHAR(100),
    Fecha_hora_llegada TIMESTAMP,
    A_Planta BOOLEAN,
    Fecha_hora_salida TIMESTAMP NOT NULL,
    Codigo_Puerto VARCHAR(10)
);

CREATE TABLE Barco (
    Matricula VARCHAR(20),
    Nombre VARCHAR(100) NOT NULL,
    Capacidad_bodega DECIMAL(10, 2),
    Tipo_Operacion VARCHAR(50)
);

CREATE TABLE Tripulante (
    Tipo_Doc VARCHAR(10),
    Nro_Doc VARCHAR(20),
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Remuneracion DECIMAL(10, 2),
    Rol VARCHAR(50),
    Experiencia VARCHAR(50)
);

CREATE TABLE Inspector (
    Matricula VARCHAR(20),
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20),
    Fecha_Designacion DATE
);

CREATE TABLE Zona (
    CodigoZona INT,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion VARCHAR(255),
    Km2 DECIMAL(10, 2)
);

-- TABLAS DE TRANSACCIONES Y DETALLES (Conjunto 1 y 2)
CREATE TABLE Pedido (
    Codigo_Pedido INT,
    Condicion_Entrega VARCHAR(50),
    Fecha_Emision DATE NOT NULL,
    CUIT_Lugar VARCHAR(13) NOT NULL,
    Codigo_Lugar VARCHAR(10) NOT NULL
);

CREATE TABLE Detalle_Pedido (
    Codigo_Pedido INT NOT NULL,
    Renglon INT NOT NULL,
    CodProdDerivado VARCHAR(20) NOT NULL,
    Cant INT NOT NULL
);

CREATE TABLE Factura (
    Nro_Serie INT NOT NULL,
    Nro INT NOT NULL,
    Fecha_emision DATE NOT NULL,
    Metodo_pago VARCHAR(50),
    Importe_total DECIMAL(10, 2) NOT NULL,
    CUIT VARCHAR(13) NOT NULL
);

CREATE TABLE Detalle_Factura (
    Nro_Serie_Factura INT NOT NULL,
    Nro_Factura INT NOT NULL,
    Renglon INT NOT NULL,
    CodProdDerivado VARCHAR(20) NOT NULL,
    Cant INT NOT NULL
);

CREATE TABLE Lote_Produccion (
    Codigo_Lote INT,
    Fecha DATE NOT NULL,
    Codigo_Planta VARCHAR(100) NOT NULL,
    Destino VARCHAR(100),
    Precio DECIMAL(10, 2),
    Sugerido VARCHAR(50),
    CodProdDerivado VARCHAR(20) NOT NULL,
    CantProdDerivado INT NOT NULL,
    CodProdCampania VARCHAR(20),
    Codigo_Especie INT NOT NULL,
    Codigo_Traslado INT,
    CantTraslado INT
);

CREATE TABLE Campana (
    CodigoCampania INT,
    Duracion INTERVAL,
    Fecha_Inicio DATE,
    Fecha_Fin DATE,
    CodigoZona INT,
    Matricula_Barco VARCHAR(20),
    CodigoPuertoSalida VARCHAR(10),
    CodigoPuertoLlegada VARCHAR(10),
    Fecha_hora_salida TIMESTAMP,
    Fecha_hora_llegada TIMESTAMP
);

CREATE TABLE Informe (
    CodInforme INT,
    Tipo VARCHAR(50),
    Observaciones TEXT,
    Fecha_Emision DATE,
    CodigoCampania INT NOT NULL,
    Matricula_Inspector VARCHAR(20) NOT NULL
);

CREATE TABLE Acta (
    CodActa INT,
    Detalle TEXT,
    Importe DECIMAL(10, 2),
    Estado VARCHAR(50),
    Fecha_Emision DATE,
    Matricula_Inspector VARCHAR(20) NOT NULL,
    CodigoCampania INT NOT NULL
);


-- TABLAS DE RELACIONES N:M (Conjunto 1 y 2)
CREATE TABLE Lleva_Especie (
    Codigo_Traslado INT NOT NULL,
    Codigo_Especie INT NOT NULL,
    Volumen DECIMAL(10, 2)
);

CREATE TABLE Participa_En (
    Tipo_Doc_Chofer VARCHAR(10) NOT NULL,
    Nro_Doc_Chofer VARCHAR(20) NOT NULL,
    Codigo_Traslado INT NOT NULL,
    Horas_Manejadas INTERVAL
);

CREATE TABLE Maneja (
    Patente VARCHAR(10) NOT NULL,
    Tipo_Doc_Chofer VARCHAR(10) NOT NULL,
    Nro_Doc_Chofer VARCHAR(20) NOT NULL
);

CREATE TABLE Procesa (
    Tipo_Doc_Trabajador VARCHAR(10) NOT NULL,
    Nro_Doc_Trabajador VARCHAR(20) NOT NULL,
    Codigo_Lote INT NOT NULL,
    Fecha DATE NOT NULL,
    Horas_Trabajadas INTERVAL,
    Cant INT
);

CREATE TABLE Llega_a (
    Codigo_Lugar VARCHAR(10) NOT NULL,
    Codigo_Traslado INT NOT NULL,
    Distancia_Recorrida DECIMAL(8, 2),
    Tipo VARCHAR(50),
    Fecha_hora TIMESTAMP
);

CREATE TABLE Sale_de (
    Codigo_Lugar VARCHAR(10) NOT NULL,
    Codigo_Traslado INT NOT NULL,
    Tipo VARCHAR(50),
    Fecha_hora TIMESTAMP
);

CREATE TABLE Asignado_a (
    Matricula_Barco VARCHAR(20) NOT NULL,
    Tipo_Doc_Tripulante VARCHAR(10) NOT NULL,
    Nro_Doc_Tripulante VARCHAR(20) NOT NULL
);

CREATE TABLE Licencia (
    CodigoLicencia INT,
    Nombre VARCHAR(100) NOT NULL,
    Tipo_Doc_Tripulante VARCHAR(10) NOT NULL,
    Nro_Doc_Tripulante VARCHAR(20) NOT NULL
);

CREATE TABLE Participa_Campana (
    CodigoCampania INT NOT NULL,
    Tipo_Doc_Tripulante VARCHAR(10) NOT NULL,
    Nro_Doc_Tripulante VARCHAR(20) NOT NULL,
    Tiempo_Valor_Por_Hora INTERVAL
);

CREATE TABLE Controla (
    Matricula_Inspector VARCHAR(20) NOT NULL,
    CodigoCampania INT NOT NULL
);

CREATE TABLE Captura (
    CodigoEspecie INT NOT NULL,
    CodigoCampania INT NOT NULL,
    Volumen_captura DECIMAL(10, 2)
);

-- ****************************************************
-- 3. DEFINICIÓN DE CLAVES PRIMARIAS (PK)
-- ****************************************************

ALTER TABLE Provincia ADD CONSTRAINT p_kprovincia PRIMARY KEY(Codigo_Provincia);
ALTER TABLE Localidad ADD CONSTRAINT p_klocalidad PRIMARY KEY(Codigo_Postal);
ALTER TABLE Producto_Derivado ADD CONSTRAINT p_kproderivado PRIMARY KEY(CodProdDerivado);
ALTER TABLE Especie ADD CONSTRAINT p_kespecie PRIMARY KEY(Codigo_Especie);
ALTER TABLE Camion ADD CONSTRAINT p_kcamion PRIMARY KEY(Patente);
ALTER TABLE Chofer ADD CONSTRAINT p_kchofer PRIMARY KEY(Tipo_Doc, Nro_Doc);
ALTER TABLE Cliente ADD CONSTRAINT p_kcliente PRIMARY KEY(CUIT);
ALTER TABLE Planta_Procesamiento ADD CONSTRAINT p_kplanta PRIMARY KEY(Nombre);
ALTER TABLE Trabajador_de_Planta ADD CONSTRAINT p_ktrabajador PRIMARY KEY(Tipo_Doc, Nro_Doc);
ALTER TABLE Puerto ADD CONSTRAINT p_kpuerto PRIMARY KEY(Codigo_Puerto);
ALTER TABLE Lugar ADD CONSTRAINT p_klugar PRIMARY KEY(Codigo_Lugar);
ALTER TABLE Factura ADD CONSTRAINT p_kfactura PRIMARY KEY(Nro_Serie, Nro);
ALTER TABLE Traslado ADD CONSTRAINT p_ktraslado PRIMARY KEY(Codigo_Traslado);
ALTER TABLE Lote_Produccion ADD CONSTRAINT p_klote PRIMARY KEY(Codigo_Lote);
ALTER TABLE Pedido ADD CONSTRAINT p_kpedido PRIMARY KEY(Codigo_Pedido);
ALTER TABLE Detalle_Factura ADD CONSTRAINT p_kdetallefactura PRIMARY KEY(Nro_Serie_Factura, Nro_Factura, Renglon);
ALTER TABLE Detalle_Pedido ADD CONSTRAINT p_kdetallepedido PRIMARY KEY(Codigo_Pedido, Renglon);
ALTER TABLE Instalacion ADD CONSTRAINT p_kinstalacion PRIMARY KEY(Numero, Codigo_Planta);
ALTER TABLE Lleva_Especie ADD CONSTRAINT p_klleaespecie PRIMARY KEY(Codigo_Traslado, Codigo_Especie);
ALTER TABLE Participa_En ADD CONSTRAINT p_kparticipaen PRIMARY KEY(Tipo_Doc_Chofer, Nro_Doc_Chofer, Codigo_Traslado);
ALTER TABLE Maneja ADD CONSTRAINT p_kmaneja PRIMARY KEY(Patente, Tipo_Doc_Chofer, Nro_Doc_Chofer);
ALTER TABLE Procesa ADD CONSTRAINT p_kprocesa PRIMARY KEY(Tipo_Doc_Trabajador, Nro_Doc_Trabajador, Codigo_Lote);
ALTER TABLE Llega_a ADD CONSTRAINT p_kllegaa PRIMARY KEY(Codigo_Lugar, Codigo_Traslado);
ALTER TABLE Sale_de ADD CONSTRAINT p_ksalede PRIMARY KEY(Codigo_Lugar, Codigo_Traslado);

-- PKs DEL CONJUNTO 2 (Captura y Control)
ALTER TABLE Barco ADD CONSTRAINT p_kbarco PRIMARY KEY(Matricula);
ALTER TABLE Tripulante ADD CONSTRAINT p_ktripulante PRIMARY KEY(Tipo_Doc, Nro_Doc);
ALTER TABLE Licencia ADD CONSTRAINT p_klicencia PRIMARY KEY(CodigoLicencia);
ALTER TABLE Zona ADD CONSTRAINT p_kzona PRIMARY KEY(CodigoZona);
ALTER TABLE Campana ADD CONSTRAINT p_kcampana PRIMARY KEY(CodigoCampania);
ALTER TABLE Inspector ADD CONSTRAINT p_kinspector PRIMARY KEY(Matricula);
ALTER TABLE Informe ADD CONSTRAINT p_kinforme PRIMARY KEY(CodInforme);
ALTER TABLE Acta ADD CONSTRAINT p_kacta PRIMARY KEY(CodActa);
ALTER TABLE Asignado_a ADD CONSTRAINT p_kasignadoa PRIMARY KEY(Matricula_Barco, Tipo_Doc_Tripulante, Nro_Doc_Tripulante);
ALTER TABLE Participa_Campana ADD CONSTRAINT p_kparticipacampana PRIMARY KEY(CodigoCampania, Tipo_Doc_Tripulante, Nro_Doc_Tripulante);
ALTER TABLE Controla ADD CONSTRAINT p_kcontrola PRIMARY KEY(Matricula_Inspector, CodigoCampania);
ALTER TABLE Captura ADD CONSTRAINT p_kcaptura PRIMARY KEY(CodigoEspecie, CodigoCampania);

-- ****************************************************
-- 4. DEFINICIÓN DE CLAVES FORÁNEAS (FK)
-- ****************************************************

-- GEOGRAFÍA Y CLIENTES (Conjunto 1)
ALTER TABLE Localidad ADD CONSTRAINT f_klocalidad_provincia FOREIGN KEY(Codigo_Provincia) REFERENCES Provincia (Codigo_Provincia);
ALTER TABLE Cliente ADD CONSTRAINT f_kcliente_localidad FOREIGN KEY(Codigo_Postal) REFERENCES Localidad (Codigo_Postal);
ALTER TABLE Planta_Procesamiento ADD CONSTRAINT f_kplanta_localidad FOREIGN KEY(Codigo_Postal) REFERENCES Localidad (Codigo_Postal);
ALTER TABLE Puerto ADD CONSTRAINT f_kpuerto_localidad FOREIGN KEY(Codigo_Postal) REFERENCES Localidad (Codigo_Postal);
ALTER TABLE Lugar ADD CONSTRAINT f_klugar_localidad FOREIGN KEY(Codigo_Postal) REFERENCES Localidad (Codigo_Postal);
ALTER TABLE Trabajador_de_Planta ADD CONSTRAINT f_ktrabajador_planta FOREIGN KEY(Codigo_Planta) REFERENCES Planta_Procesamiento (Nombre);
ALTER TABLE Instalacion ADD CONSTRAINT f_kinstalacion_planta FOREIGN KEY(Codigo_Planta) REFERENCES Planta_Procesamiento (Nombre);

-- TRANSACCIONES DE COMERCIALIZACIÓN (Conjunto 1)
ALTER TABLE Factura ADD CONSTRAINT f_kfactura_cliente FOREIGN KEY(CUIT) REFERENCES Cliente (CUIT);
ALTER TABLE Detalle_Factura ADD CONSTRAINT f_kdfactura_factura FOREIGN KEY(Nro_Serie_Factura, Nro_Factura) REFERENCES Factura (Nro_Serie, Nro);
ALTER TABLE Detalle_Factura ADD CONSTRAINT f_kdfactura_producto FOREIGN KEY(CodProdDerivado) REFERENCES Producto_Derivado (CodProdDerivado);
ALTER TABLE Pedido ADD CONSTRAINT f_kpedido_cliente FOREIGN KEY(CUIT_Lugar) REFERENCES Cliente (CUIT);
ALTER TABLE Pedido ADD CONSTRAINT f_kpedido_lugar FOREIGN KEY(Codigo_Lugar) REFERENCES Lugar (Codigo_Lugar);
ALTER TABLE Detalle_Pedido ADD CONSTRAINT f_kdpedido_pedido FOREIGN KEY(Codigo_Pedido) REFERENCES Pedido (Codigo_Pedido);
ALTER TABLE Detalle_Pedido ADD CONSTRAINT f_kdpedido_producto FOREIGN KEY(CodProdDerivado) REFERENCES Producto_Derivado (CodProdDerivado);

-- LOGÍSTICA (Conjunto 1)
ALTER TABLE Traslado ADD CONSTRAINT f_ktraslado_camion FOREIGN KEY(Patente) REFERENCES Camion (Patente);
ALTER TABLE Traslado ADD CONSTRAINT f_ktraslado_puerto FOREIGN KEY(Codigo_Puerto) REFERENCES Puerto (Codigo_Puerto);
ALTER TABLE Traslado ADD CONSTRAINT f_ktraslado_planta_salida FOREIGN KEY(Codigo_Planta_Salida) REFERENCES Planta_Procesamiento (Nombre);
ALTER TABLE Traslado ADD CONSTRAINT f_ktraslado_planta_llegada FOREIGN KEY(Codigo_Planta_Llegada) REFERENCES Planta_Procesamiento (Nombre);
ALTER TABLE Participa_En ADD CONSTRAINT f_kparticipaen_chofer FOREIGN KEY(Tipo_Doc_Chofer, Nro_Doc_Chofer) REFERENCES Chofer (Tipo_Doc, Nro_Doc);
ALTER TABLE Participa_En ADD CONSTRAINT f_kparticipaen_traslado FOREIGN KEY(Codigo_Traslado) REFERENCES Traslado (Codigo_Traslado);
ALTER TABLE Maneja ADD CONSTRAINT f_kmaneja_chofer FOREIGN KEY(Tipo_Doc_Chofer, Nro_Doc_Chofer) REFERENCES Chofer (Tipo_Doc, Nro_Doc);
ALTER TABLE Maneja ADD CONSTRAINT f_kmaneja_camion FOREIGN KEY(Patente) REFERENCES Camion (Patente);
ALTER TABLE Lleva_Especie ADD CONSTRAINT f_klleaespecie_traslado FOREIGN KEY(Codigo_Traslado) REFERENCES Traslado (Codigo_Traslado);
ALTER TABLE Lleva_Especie ADD CONSTRAINT f_klleaespecie_especie FOREIGN KEY(Codigo_Especie) REFERENCES Especie (Codigo_Especie);
ALTER TABLE Llega_a ADD CONSTRAINT f_kllegaa_lugar FOREIGN KEY(Codigo_Lugar) REFERENCES Lugar (Codigo_Lugar);
ALTER TABLE Llega_a ADD CONSTRAINT f_kllegaa_traslado FOREIGN KEY(Codigo_Traslado) REFERENCES Traslado (Codigo_Traslado);
ALTER TABLE Sale_de ADD CONSTRAINT f_ksalede_lugar FOREIGN KEY(Codigo_Lugar) REFERENCES Lugar (Codigo_Lugar);
ALTER TABLE Sale_de ADD CONSTRAINT f_ksalede_traslado FOREIGN KEY(Codigo_Traslado) REFERENCES Traslado (Codigo_Traslado);

-- PRODUCCIÓN (Conjunto 1)
ALTER TABLE Lote_Produccion ADD CONSTRAINT f_klote_planta FOREIGN KEY(Codigo_Planta) REFERENCES Planta_Procesamiento (Nombre);
ALTER TABLE Lote_Produccion ADD CONSTRAINT f_klote_producto FOREIGN KEY(CodProdDerivado) REFERENCES Producto_Derivado (CodProdDerivado);
ALTER TABLE Lote_Produccion ADD CONSTRAINT f_klote_especie FOREIGN KEY(Codigo_Especie) REFERENCES Especie (Codigo_Especie);
ALTER TABLE Lote_Produccion ADD CONSTRAINT f_klote_traslado FOREIGN KEY(Codigo_Traslado) REFERENCES Traslado (Codigo_Traslado);
ALTER TABLE Procesa ADD CONSTRAINT f_kprocesa_trabajador FOREIGN KEY(Tipo_Doc_Trabajador, Nro_Doc_Trabajador) REFERENCES Trabajador_de_Planta (Tipo_Doc, Nro_Doc);
ALTER TABLE Procesa ADD CONSTRAINT f_kprocesa_lote FOREIGN KEY(Codigo_Lote) REFERENCES Lote_Produccion (Codigo_Lote);

-- CAPTURA Y CONTROL (Conjunto 2)
ALTER TABLE Campana ADD CONSTRAINT f_kcampana_zona FOREIGN KEY(CodigoZona) REFERENCES Zona (CodigoZona);
ALTER TABLE Campana ADD CONSTRAINT f_kcampana_barco FOREIGN KEY(Matricula_Barco) REFERENCES Barco (Matricula);
ALTER TABLE Campana ADD CONSTRAINT f_kcampana_puerto_salida FOREIGN KEY(CodigoPuertoSalida) REFERENCES Puerto (Codigo_Puerto);
ALTER TABLE Campana ADD CONSTRAINT f_kcampana_puerto_llegada FOREIGN KEY(CodigoPuertoLlegada) REFERENCES Puerto (Codigo_Puerto);

ALTER TABLE Licencia ADD CONSTRAINT f_klicencia_tripulante FOREIGN KEY(Tipo_Doc_Tripulante, Nro_Doc_Tripulante) REFERENCES Tripulante (Tipo_Doc, Nro_Doc);
ALTER TABLE Asignado_a ADD CONSTRAINT f_kasignadoa_barco FOREIGN KEY(Matricula_Barco) REFERENCES Barco (Matricula);
ALTER TABLE Asignado_a ADD CONSTRAINT f_kasignadoa_tripulante FOREIGN KEY(Tipo_Doc_Tripulante, Nro_Doc_Tripulante) REFERENCES Tripulante (Tipo_Doc, Nro_Doc);
ALTER TABLE Participa_Campana ADD CONSTRAINT f_kparticipacampana_tripulante FOREIGN KEY(Tipo_Doc_Tripulante, Nro_Doc_Tripulante) REFERENCES Tripulante (Tipo_Doc, Nro_Doc);
ALTER TABLE Participa_Campana ADD CONSTRAINT f_kparticipacampana_campana FOREIGN KEY(CodigoCampania) REFERENCES Campana (CodigoCampania);

ALTER TABLE Informe ADD CONSTRAINT f_kinforme_inspector FOREIGN KEY(Matricula_Inspector) REFERENCES Inspector (Matricula);
ALTER TABLE Informe ADD CONSTRAINT f_kinforme_campana FOREIGN KEY(CodigoCampania) REFERENCES Campana (CodigoCampania);
ALTER TABLE Acta ADD CONSTRAINT f_kacta_inspector FOREIGN KEY(Matricula_Inspector) REFERENCES Inspector (Matricula);
ALTER TABLE Acta ADD CONSTRAINT f_kacta_campana FOREIGN KEY(CodigoCampania) REFERENCES Campana (CodigoCampania);
ALTER TABLE Controla ADD CONSTRAINT f_kcontrola_inspector FOREIGN KEY(Matricula_Inspector) REFERENCES Inspector (Matricula);
ALTER TABLE Controla ADD CONSTRAINT f_kcontrola_campana FOREIGN KEY(CodigoCampania) REFERENCES Campana (CodigoCampania);
ALTER TABLE Captura ADD CONSTRAINT f_kcaptura_campana FOREIGN KEY(CodigoCampania) REFERENCES Campana (CodigoCampania);
ALTER TABLE Captura ADD CONSTRAINT f_kcaptura_especie FOREIGN KEY(CodigoEspecie) REFERENCES Especie (Codigo_Especie);
```
