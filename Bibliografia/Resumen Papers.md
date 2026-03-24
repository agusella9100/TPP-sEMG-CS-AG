Resumen Papers :



## **"Una interfaz neuromotora genérica no invasiva para la interacción humano-computadora"**

###### 

###### **Citar este artículo**

###### **Kaifosh, P., Reardon, T.R. \& CTRL-labs en Reality Labs. Una interfaz neuromotora genérica no invasiva para la interacción humano-computadora. Naturaleza (2025). https://doi.org/10.1038/s41586-025-09255-w**



**Problema: cámaras o sensores inerciales para evitar un dispositivo intermediario, pero tienden a funcionar bien solo para movimientos no oscurecidos. interfaces cerebro-computadora o neuromotoras que interactúan directamente con la señalización eléctrica del cuerpo resuelven el problema de la interfaz1, pero la comunicación de gran ancho de banda se ha demostrado solo utilizando interfaces invasivas con decodificadores a medida diseñados para individuos individuales**



**Solucion1: interfaz neuromotora genérica no invasiva que permite la entrada de la computadora decodificada a partir de la electromiografía de superficie (sEMG). Pulsera sensible, sencilla de aplicar y escalable para juntar datos y decodificar datos de entrenamiento.**



**Enfoques no invasivos basados en el registro del electroencefalograma (EEG)6 Las señales en el cuero cabelludo han ofrecido más generalidad entre las personas, por ejemplo, para los juegos (Kerous, B., Skola, F. \& Liarokapis, F. EEG-based BCI and video games: a progress report. Virtual Reality 22, 119–135 (2018). https://doi.org/10.1007/s10055-017-0328-x)**







**There are still limitations in detection and**

**characterization of existing nonlinearities in the surface**

**electromyography (sEMG, a special technique for**

**studying muscle signals) signal, estimation of the phase,**

**acquiring exact information due to derivation from**

**normality**



Las grabaciones de EMG de superficie (sEMG) ofrecen una alta relación señal-ruido al amplificar las señales neuronales en el músculo



Aplicaciones clínicas emg (https://doi.org/10.1123/jab.13.2.135) rehabilitación y control prostetico (D. Farina et al., "The Extraction of Neural Information from the Surface EMG for the Control of Upper-Limb Prostheses: Emerging Avenues and Challenges," in IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 22, no. 4, pp. 797-809, July 2014, doi: 10.1109/TNSRE.2014.2305111. keywords: {Electromyography;Muscles;Electric potential;Neurons;Electrodes;Crosstalk;Feature extraction;Motor unit;myoelectric control;neural drive to muscle;pattern recognition;regression},    Surface EMG in Clinical Assessment and Neurorehabilitation: Barriers Limiting Its Use https://doi.org/10.1123/jab.13.2.135 Carlo J. De Luca )









Using a Common Average Reference to Improve Cortical Neuron Recordings From Microelectrode Arrays

Kip A. Ludwig, Rachel M. Miriani, Nicholas B. Langhals, Michael D. Joseph, David J. Anderson, and Daryl R. Kipke

Journal of Neurophysiology 2009 101:3, 1679-1689
https://journals.physiology.org/doi/full/10.1152/jn.90989.2008











IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 49, NO. 3, JUNE 2000 535A Comprehensive Model for Power Line Interferencein Biopotential Measurements
https://doi.org/10.1109/19.850390

Es en ecg pero sirve para comprender.

Identifican 4 fuentes de interferencia de linea.

1. Inducción magnética en las entradas (electrodos supongo)
2. corrientes de desplazamiento (por campo magentico) en los electrodos

3\) corrientes de desplazamiento en el cuerpo

4\) tensión de modo común por el no rechazo del opamp. Un DRL reduce esto.

Se considera la reducción paraa amplificadores aislados y no aislados. Mejorar CMRR de diferentes maneras como mejorando la impedancia de aislación Zce



Importancia de acoplamiento capacitivo de las tensiones a los cables de electrodos. Como el blindaje de los cables no se extiende a los electrodos, es una solución limitada.
Se debe considerar la interferencia raiada por los cables de la alimentación

En circuitos de electrodos no es posible tener una baja impedancia de guarda en la coneccion debido a que los electrodos son de alta impedancia.
Aca proponen un modelo para considerar estas fuentes.

En la figura 1 ponen el modelo con la tensión de alimentación y impedancias para el cuerpo, electrodos, capacidades de acople de electrodos, las de acople a tierra-paciente. impedancias de las entradas diferenciales y comunes. Ziso es la impedancia de aislación.



La máxima contribución de interferencia viene de corrientes de desplacamiento acopladas al cuerpo y a los electrodos. el resto son medio despreciables dice.

Toman como tensión de interferencia a Vn = Vd + Vcm/Cmrr + Viso/Imrr ; donde Vd es la tensión diferencial de interferencia ; Viso es la de interferencia por la aislación ¿? .

 Como bajar la interferencia según impedancias:

\-> Si tengo alta impedancia de paciente-alimentación Zp (depednde de cercania con la fuente)

\-> Si tengo baja impedancia de paciente a tierra Zb (pero debe ser suficientemente alta para su seguridad, cuanto mas cerca a tierra el paciente)



Regulaciones de seguridad dicen mínimo 22Mohm de impedancia de aislacion

 
Método simple para reducir interferencia del paciente es cubrirlo con papel aluminio conectado al común del amplificador (actúa como blindaje eléctrico).
Blindajes activos conectan un ampli directo al electrodo usando un cable corto mantienen la alta impedancia y reducen las corrientes de desplazamiento en los electrodos (esta segunda mata la interferencia de 50Hz).

Una conclusión es q los modelos de interferencia de linea no pueden explicar la interferencia en sistemas que usan blindajes de electrodos y amplificadores con alto cmrr e imrr. Igualmente se atribuye la mayoría de la interferencia a electrodos no blindados.

Resumen de lo mejor : Electrodos blindados reducen la interferencia y electrodos activos mantienen la impedancia alta de entrada.

