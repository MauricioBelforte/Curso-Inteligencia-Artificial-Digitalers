class ApplicationComponent {
    constructor(parent) {
        this.parent = parent;
        this.model = new Fintech();
        this.model.crearCliente("Juan", "educacionit@gmail.com", "intropoo", "intropoo");
        this.model.crearCliente("Pedro", "intropoo@gmail.com", "intropoo", "intropoo");
        this.router = new Router(this.parent, this.model)
        this.router.navigateTo(LoginComponent);
    }
}