# Best Practices for building Python Applications
1. Use Python 3 (Python 2 is not supported since Jan, 2020)
2. Check memory usage for your objects
3. Use Data classes over regular classes
4. Create a progress bar (or use `progress` package)
5. Write tests for your application
6. Use linters and formatters
7. Update your dependencies
8. Scan and test for security vulnerabilities 
9. Increase observability of your application (metrics, logging, etc..)
10. KISS principle (Keep It Stupid Simple)

#  Best Practices for building Python applications with Docker

1. Keep the image size to minimum
2. Keep the application stateless
3. Use CI/CD for testing and deployment
4. Avoid hard-coding. Make it externally configurable (environment variables, config files, etc..)
5. Don't "Run as Root", it is insecure
6. Cache your dependencies (Nexus, artifactory, etc..)
7. Make it observable
8. One Container = One process
9. Move web applications and background workers to separate containers
10. Reduce the amount of layers and put them in order to use caching abilities