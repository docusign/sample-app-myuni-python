import React, { Suspense } from "react";
import { Route, Switch } from "react-router-dom";
import Layout from "./components/Layout";
import { About } from "./features/About";
import { History } from "./features/History";
import { Home } from "./features/Home";
import { RequestMajorMinorChangePage } from "./features/RequestMajorMinorChange";
import { RequestTranscriptPage } from "./features/RequestTranscript";
import { RequestExtracurricularActivityPage } from "./features/RequestExtracurricularActivity";
import { SigningComplete } from "./components/SigningComplete.js";
import "./assets/scss/main.scss";

const App = () => {
  const routes = (
    <Switch>
      <Route path="/history" component={History} />
      <Route path="/about" component={About} />
      <Route
        path="/requestMajorMinorChange"
        component={RequestMajorMinorChangePage}
      />
      <Route path="/requestTranscript" component={RequestTranscriptPage} />
      <Route
        path="/requestExtracurricularActivity"
        component={RequestExtracurricularActivityPage}
      />
      <Route path="/" exact component={Home} />
      <Route path="/signing_complete" component={SigningComplete} />
    </Switch>
  );
  return (
    <Suspense fallback="">
      <Layout>{routes}</Layout>
    </Suspense>
  );
};

export default App;
