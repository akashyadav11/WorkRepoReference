
## sja
Spring Boot allows you to create operating, production-grade, stand-alone Spring based Applications with ease.

Spring Boot Framework

is an opinionated framework.

is based on convention over configuration.

can build stand-alone applications.

can create a production-ready package.

has Embedded Tomcat server.

To summarize, Spring Boot Framework is a pre-configured, pre-sugared set of technologies/framework to minimize boilerplate configuration offering the quickest way to get a Spring web application ready and operational with minimal configuration/coding out-of-the-box.


Bean:  bean is java object , which is managed by spring container (IOC Container)
IOC container contains all beans which get created and also manage them 
Beans can be created using @bean and @Component annonation
Components follows convention over configuration approach ->Means spring boot will try to auto config based on convention reducing the need of explicit configuration   

--@controller ,@service all are internally tells spring to create bean and manage it 
ComponentScan will scan the specific package and sub-package for class annotated with @Component,@Service etc  

2 ways to create beans 1 .Eagerness :bean with sigleton scope are eager intialized   
 2.Lazy : scope like prototype are lazily intialized  


 ## How to start 
 Here are the steps to build a simple Spring boot application.

Generate a quick Java project with Maven command.

Update pom.xml with the Spring web and other Spring boot dependencies.

Add SpringApplication.run() method to bootstrap Spring application.

Do a Maven clean build using mvn clean package command.

Execute command mvn spring-boot:run to run the application.
## SQL Databases - Integration
Spring Boot Framework is quite flexible while working with SQL database. You can use direct JDBC calls using JDBC templates, or you can go by implementing hibernate.

One more significant option that Spring framework offers is by creating repositories for Spring Data implementation.
## JPA 
What is JPA?

Java Persistence API is a specification that lets you do Object-Relational Mapping (ORM) over a relational database.

What is ORM?

ORM allows you to map the entity classes to your relational SQL database.

What is Spring Data JPA?

Spring Framework handles ORM in an easy and quick fashion using JPA.

## security
Spring Security can be broadly classified as

Authentication

Authorization

Spring Security architecture distinguishes both authentication and authorization.

Authentication

The interface defined for Authentication is Authentication Manager. This is a single method Interface.

public interface AuthenticationManager {
  Authentication authenticate(Authentication authentication)
    throws AuthenticationException;
}