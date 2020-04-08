import React from "react";
import { Link, NavLink } from "react-router-dom";
import svg from "../assets/img/logo.svg";
import { useTranslation } from "react-i18next";

export const Header = () => {
  const { t } = useTranslation("Common");
  return (
    <header className="header" role="banner">
      <div className="container-fluid">
        <nav className="navbar navbar-expand-lg navbar-light p-0 align-items-lg-end">
          <Link
            className="navbar-brand d-inline-flex align-items-end p-0"
            to="/"
          >
            <span className="navbar-brand-image d-inline-block">
              <img src={svg} alt="DocuSign logo" />
            </span>
            {t("ApplicationName")}
          </Link>
          <button
            className="navbar-toggler collapsed"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="line"></span>
            <span className="line"></span>
            <span className="line"></span>
          </button>
          <div
            className="collapse navbar-collapse justify-content-md-end"
            id="navbarNav"
          >
            <ul className="navbar-nav">
              <li className="nav-item">
                <a
                  className="nav-link"
                  href="https://github.com/docusign/sample-app-myuni-python"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {t("GitHubLink")}
                </a>
              </li>
              <li className="nav-item">
                <NavLink
                  className="nav-link"
                  activeClassName="active"
                  to="/history"
                >
                  {t("TransactionHistoryLink")}
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/about">
                  {t("AboutLink")}
                </NavLink>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </header>
  );
};
