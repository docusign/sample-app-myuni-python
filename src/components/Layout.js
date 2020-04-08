import React from "react";
import { Header } from "./Header";
import { Footer } from "./Footer";
import { useTranslation } from "react-i18next";
import { Helmet } from "react-helmet";

const Layout = props => {
  const { t } = useTranslation("Common");
  return (
    <>
      <Helmet>
        <title>{t("MyUni DocuSign Sample Application")}</title>
        <meta name="description" content={t("MetaDescription")}/>
      </Helmet>
      <Header />
      <main role="main" className="content">
        {props.children}
      </main>
      <Footer />
    </>
  );
};

export default Layout;
