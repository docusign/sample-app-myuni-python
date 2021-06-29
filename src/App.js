import React, { Suspense, useState, useEffect } from "react";
import { Route, Switch } from "react-router-dom";
import Layout from "./components/Layout";
import { About } from "./features/About";
import { History } from "./features/History";
import { Home } from "./features/Home";
import { RequestMajorMinorChangePage } from "./features/RequestMajorMinorChange";
import { RequestTranscriptPage } from "./features/RequestTranscript";
import { RequestExtracurricularActivityPage } from "./features/RequestExtracurricularActivity";
import { SigningComplete } from "./components/SigningComplete.js";
import { logOut, getStatus } from "./api/auth";
import { Callback } from "./components/Callback";
import history from "./api/history";
import "./assets/scss/main.scss";
import LoggedUserContext from "./contexts/logged-user/logged-user.context";


const App = () => {
  const [ logged, setLogged ] = useState(false);
  const [ redirectUrl, setRedirectUrl ] = useState("/");
  const [ showAlert, setShowAlert ] = useState(false);
  const [ showJWTModal, setShowJWTModal] = useState(false);
  const [ authType, setAuthType ] = useState(undefined);

  useEffect(() => {
    getStatus(setLogged, setAuthType);
  }, []);

  async function handleLogOut() {
    await logOut();
    history.push("/");
    getStatus(setLogged, setAuthType);
  }

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
      <Route path="/callback" component={Callback}/>
      <Route path="/logout" render={() => {
        handleLogOut();
      }} />
    </Switch>
  );

  return (
    <Suspense fallback="">
      <LoggedUserContext.Provider value={{ logged, setLogged, redirectUrl, setRedirectUrl, 
                                          showAlert, setShowAlert, showJWTModal, setShowJWTModal, 
                                          authType, setAuthType}}>
        <Layout>{routes}</Layout>
      </LoggedUserContext.Provider>
    </Suspense>
  );
};

export default App;