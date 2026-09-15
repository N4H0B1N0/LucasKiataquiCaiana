#include "crow.h"

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/")([](){
        auto page = crow::mustache::load("index.html");
        return page.render();
    });

    CROW_ROUTE(app, "/sobre")([](){
        auto page = crow::mustache::load("sobre.html");
        return page.render();
    });

    CROW_ROUTE(app, "/contato")([](){
        auto page = crow::mustache::load("contato.html");
        return page.render();
    });

    app.port(18080).multithreaded().run();
}
