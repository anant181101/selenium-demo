from pages.search_page import PythonOrgSearchPage


def test_search_python_site(chrome):
    page = PythonOrgSearchPage(chrome)
    page.open_home()
    page.enter_query("selenium")
    page.submit_search()

    assert page.has_results()
