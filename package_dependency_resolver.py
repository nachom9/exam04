
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:




    return result


print(package_dependency_resolver({"app": ["database"], "aap": ["database"], "database": ["driver"], "driver": [], "diver": []}))
print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))