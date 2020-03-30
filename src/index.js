import React from "react";
import ReactDOM from "react-dom";
import { Router } from "react-router-dom";
import App from "./App";
import history from "./api/history";
import "./i18n";
import "bootstrap/dist/js/bootstrap.js";

const app = (
  <Router history={history}>
    <App />
  </Router>
);

ReactDOM.render(app, document.getElementById("root"));
