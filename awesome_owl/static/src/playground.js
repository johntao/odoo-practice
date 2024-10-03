/** @odoo-module **/

import { Component, markup, useState } from "@odoo/owl";
import { Counter } from "./counter";
import { Card } from "./card";
// import { TodoList } from "./todo_list";
import { TodoList } from "./todos";

export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = { Counter, Card, TodoList };
    val1 = '<a href="#">Link</a>';
    val2 = markup('<a href="#">Link</a>');
    // sum = 2;
    setup() {
        this.state = useState({ sum: 2 });
    }
    incrementSum() {
        this.state.sum++;
        // this.sum++;
    }
}
