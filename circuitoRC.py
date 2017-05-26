import numpy as np
import matplotlib.pyplot as plt

# Tomado de https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/14.MonteCarloMethods/bayes_MCMC.ipynb
carga_max=95.0
circuito=np.genfromtxt("CircuitoRC.txt")
t=circuito[:,0]
y=circuito[:,1]
I=150  #Se asume una corriente.
my_t=np.linspace(0,300)

def my_model(t,carga_max,r,c):
    y=carga_max*(1-np.exp(-t/r*c)) 
    return(y)


def likelihood(y_obs, y_model):
    chi_squared = (1.0/(90000)*2.0)*sum((y_obs-y_model)**2)
    return np.exp(-chi_squared)


r_walk = np.empty((0))
c_walk = np.empty((0))
likelihood_walk=np.empty((0))


r_walk = np.append(r_walk, np.random.random())
c_walk = np.append(c_walk, np.random.random())
y_init = my_model(t, carga_max ,r_walk[0], c_walk[0])


likelihood_walk = np.append(likelihood_walk, likelihood(y, y_init))

n_iterations = 2000 #this is the number of iterations I want to make
for i in range(n_iterations):
    r_prime = np.random.normal(r_walk[i], 0.1) 
    c_prime = np.random.normal(c_walk[i], 0.1)

    y_init = my_model(t,10*r_walk[i]*c_walk[i]*I , r_walk[i], c_walk[i])
    y_prime = my_model(t,10*r_prime*c_prime*I ,r_prime, c_prime)
    
    likelihood_prime = likelihood(y, y_prime)
    likelihood_init = likelihood(y, y_init)
    
    
    alpha = likelihood_prime/likelihood_init
    
    if(alpha>=1.0):
        r_walk  = np.append(r_walk,r_prime)
        c_walk  = np.append(c_walk,c_prime)
        likelihood_walk = np.append(likelihood_walk, likelihood_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            r_walk = np.append(r_walk,r_prime)
            c_walk = np.append(c_walk,c_prime)
            likelihood_walk = np.append(likelihood_walk, likelihood_prime)
        else:
            r_walk = np.append(r_walk,r_walk[i])
            c_walk = np.append(c_walk,c_walk[i])
            likelihood_walk = np.append(likelihood_walk, likelihood_init)



count, bins, ignored =plt.hist(c_walk, 20, normed=True)
plt.savefig('RvsLikelihood.jpg')
plt.close()
count, bins, ignored =plt.hist(r_walk, 20, normed=True)
plt.savefig('CvsLikelihood.jpg')
plt.close()


max_likelihood_id = np.argmax(likelihood_walk)
best_r = r_walk[max_likelihood_id]
best_c = c_walk[max_likelihood_id]
sc=str(best_c)
sr=str(best_r)

carga_max =   10*best_r*best_c*I         
best_y = my_model(my_t,  carga_max ,best_r,best_c)

plt.scatter(t,y)
plt.plot(my_t, best_y)

plt.text(5,120,"R=" +sr[:8])
plt.text(5,115,"C=" +sc[:8])
plt.text(5,110,"carga maxima=" +sc[:8])
plt.savefig('model.jpg')
plt.close()