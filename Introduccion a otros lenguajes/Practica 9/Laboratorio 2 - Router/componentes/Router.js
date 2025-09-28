class Router {
    constructor(parent, model) {
        this.parent = parent;
        this.model = model;
    }
    navigateTo(Componente, model) {
        let componente = new Componente(this.parent, this.model, this);
        componente.render();
    }
}