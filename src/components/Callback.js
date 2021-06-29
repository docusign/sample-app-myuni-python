import React, { useEffect, useContext } from "react";
import { completeCallback } from "../api/auth";
import LoggedUserContext from "../contexts/logged-user/logged-user.context";

export const Callback = () => {
    const { setLogged, setAuthType, setShowAlert, setShowJWTModal } = useContext(LoggedUserContext); 
    useEffect(() => {
        completeCallback(setShowAlert, setLogged, setAuthType, setShowJWTModal);
    });

    return (
        <>
        </>
    )
}
